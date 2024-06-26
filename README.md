# Camera-to-Base Station Video Streaming Application

This project showcases the integration of a custom-built camera developed by Bruce with our base station, which receives and displays the video stream. The system comprises:

1. **Camera**: Developed by bruce, this device captures video and streams it over the network.
2. **Base Station Receiver**: Our Python script receives the video stream and displays it using OpenCV.

## Requirements

- Python 3.x
- Flask (for simulating the camera in the development environment)
- OpenCV
- Requests

## Installation

First, clone this repository to your local machine. Then, install the necessary Python libraries with the following command:
## Project Structure
camera_simulator.py: Simulates the camera's streaming functionality using Flask. Replace this with the actual camera's streaming output when available.
base_station_receiver.py: Acts as the base station, connecting to the camera's stream and displaying it using OpenCV.
## Usage
Simulating the Camera
During development or testing, you can simulate the camera's stream by running the camera_simulator.py script:

### Running the Base Station Receiver

python camera_simulator.py
This script starts a server that mimics the camera's video streaming capabilities, accessible at http://0.0.0.0:5000/. The video stream can be found at http://0.0.0.0:5000/video.

### Running the Base Station Receiver
With the camera (or simulator) operational, start the base_station_receiver.py script on the same machine or a different machine within the same network:

python base_station_receiver.py

Ensure the video_url in base_station_receiver.py is correct, pointing to the camera's stream URL. If using the simulator, use http://localhost:5000/video.

### Features
Real-time Video Streaming: Seamlessly receive and display video streams from the custom-built camera at the base station.
Development Flexibility: Includes a camera simulator to facilitate testing and development without the physical camera hardware.
###Configuration
Adjust network settings to allow HTTP traffic on the port where the camera or simulator is hosted (default is 5000). Modify firewall settings as needed to accommodate this traffic.

