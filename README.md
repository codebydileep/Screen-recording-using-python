# Screen Recorder

## Overview
This is a simple screen recording application built using Python and Tkinter. It captures the screen in real-time and saves the recording as a video file.

## Features
- Start and stop screen recording with a GUI interface.
- Saves recordings in AVI format.
- Provides a live preview of the recording.
- Uses multi-threading to ensure smooth execution.

## Requirements
Ensure you have the following dependencies installed before running the script:

```bash
pip install opencv-python numpy pyautogui pillow
```

## How to Run
1. Clone or download the repository.
2. Open a terminal and navigate to the project folder.
3. Run the script using:

## Usage
- Click the "Start Recording" button to begin capturing the screen.
- Click the "Stop Recording" button to save the recording as `output.avi`.
- The preview window provides a small real-time display of the recorded content.

## File Structure
```
/ScreenRecorder
│── screen_recording.py  # Main script file
│── output.avi           # Recorded video file (generated after recording)
```

## Dependencies
- `tkinter`: GUI interface for buttons and controls.
- `pyautogui`: Captures the screen.
- `opencv-python`: Handles video processing and saving.
- `numpy`: Converts images into NumPy arrays.
- `Pillow`: Converts images for GUI preview.
- `threading`: Runs screen recording in a separate thread.

## Future Improvements
- Add custom resolution and frame rate options.
- Implement pause/resume functionality.
- Enable audio recording alongside video capture.



