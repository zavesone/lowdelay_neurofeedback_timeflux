import numpy as np
import scipy.signal as sg
from timeflux.core.node import Node
from modules.utils import individual_max_snr_band

class CFIRBandEnvelopeDetector:
    def __init__(self, fs, delay, n_taps=500, n_fft=2000, weights=None):
        self.fs = fs
        self.delay = delay
        self.n_taps = n_taps
        self.n_fft = n_fft
        self.weights = weights
        self.b = None
        self.a = np.array([1.])
        self.zi = None

    def calibrate(self, x):
        band, _ = individual_max_snr_band(x, self.fs)
        w = np.arange(self.n_fft)
        H = 2 * np.exp(-2j * np.pi * w / self.n_fft * self.delay)
        H[(w / self.n_fft * self.fs < band[0]) | (w / self.n_fft * self.fs > band[1])] = 0
        F = np.array([np.exp(-2j * np.pi / self.n_fft * k * np.arange(self.n_taps)) for k in np.arange(self.n_fft)])
        if self.weights is None:
            self.b = F.T.conj().dot(H)/self.n_fft
        else:
            W = np.diag(self.weights)
            self.b = np.linalg.solve(F.T.dot(W.dot(F.conj())), (F.T.conj()).dot(W.dot(H)))
        self.zi = np.zeros(len(self.b)-1)

    def apply(self, chunk: np.ndarray):
        if self.b is None:
            return np.zeros_like(chunk)
        y, self.zi = sg.lfilter(self.b, self.a, chunk, zi=self.zi)
        return y

class CFIRNode(Node):
    def __init__(self, fs, delay, n_taps=500, n_fft=2000, weights=None, calibration_time=60):
        self.filter = CFIRBandEnvelopeDetector(fs, delay, n_taps, n_fft, weights)
        self.calibration_data = []
        self.calibration_time = calibration_time
        self.fs = fs
        self.is_calibrated = False

    def update(self):
        if self.i.data is not None:
            if not self.is_calibrated:
                self.calibration_data.extend(self.i.data.flatten())
                if len(self.calibration_data) >= self.calibration_time * self.fs:
                    self.filter.calibrate(np.array(self.calibration_data))
                    self.is_calibrated = True
                    self.calibration_data = []
            
            self.o.data = np.abs(self.filter.apply(self.i.data))