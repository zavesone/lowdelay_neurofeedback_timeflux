## Visual Environment Demo
[![Neurofeedback Environment in UE5](https://img.youtube.com/vi/G4-PEHXkyxI/0.jpg)](https://youtu.be/G4-PEHXkyxI)

*This demo showcases the immersive environment component designed for neurofeedback training. The scene demonstrates dynamic weather system transitions from adverse to favorable conditions, which will serve as visual feedback for successful alpha rhythm training in the full implementation.*

# lowdelay_neurofeedback_timeflux
A low delay neurofeedback script made with time flux based on the paper "Short-delay neurofeedback facilitates training of the parietal alpha  rhythm"

# EEG-Driven Neurofeedback Environment in Unreal Engine 5

## Project Overview

This project combines cutting-edge neurofeedback techniques with immersive virtual reality to create a responsive, natural environment that reacts in real-time to a user's brain activity. The system uses EEG data from an open-source device to modulate the brightness of a detailed, natural environment created in Unreal Engine 5, providing immediate visual feedback to the user.

## Key Features

- Real-time EEG data processing using advanced signal processing techniques
- Low-latency neurofeedback implementation
- Immersive natural environment built in Unreal Engine 5
- Dynamic lighting system responsive to user's brain activity
- Open-source EEG hardware integration

## Technologies Used

1. **Unreal Engine 5**: For creating and rendering the immersive natural environment.

2. **FreeEEG32**: An open-source EEG device for capturing brain activity data.

3. **OpenViBE**: An open-source software platform for designing, testing, and using Brain-Computer Interfaces. Used to interface with FreeEEG32 and stream data via LSL.

4. **Lab Streaming Layer (LSL)**: For streaming EEG data with minimal latency.

5. **Timeflux**: A Python framework for building and running real-time biosignal processing pipelines.

6. **cFIR (complex-valued Finite Impulse Response) Filter**: Implemented for low-latency, accurate estimation of brain rhythm parameters.

7. **Python**: Used for data processing scripts and implementing the cFIR filter.

8. **C++**: For performance-critical components in Unreal Engine.

9. **Blueprints Visual Scripting**: For rapid prototyping and logic implementation in Unreal Engine.

## System Architecture

1. FreeEEG32 device captures brain activity.
2. OpenViBE interfaces with FreeEEG32 and streams data via LSL.
3. Timeflux receives the LSL stream and processes it using the cFIR filter.
4. Processed data is sent back out via LSL.
5. Unreal Engine 5 receives the processed data and adjusts the environment brightness accordingly.
