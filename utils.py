import numpy as np
from scipy import signal

def individual_max_snr_band(x, fs, band_width=2, lowcut=8, highcut=12):
    """Find individual alpha band with max SNR"""
    bands = [(f, f+band_width) for f in np.arange(lowcut, highcut-band_width+1, 0.5)]
    snrs = [snr_band(x, fs, band) for band in bands]
    max_snr_band = bands[np.argmax(snrs)]
    return max_snr_band, np.max(snrs)

def snr_band(x, fs, band):
    """SNR in specific band"""
    x_filt = band_hilbert(x, fs, band)
    snr = 10 * np.log10(np.var(x_filt) / np.var(x - x_filt))
    return snr

def band_hilbert(x, fs, band):
    """Band-pass filter and perform Hilbert transform"""
    nyq = fs / 2
    b, a = signal.butter(3, [band[0] / nyq, band[1] / nyq], btype='band')
    x_filt = signal.filtfilt(b, a, x)
    return signal.hilbert(x_filt)