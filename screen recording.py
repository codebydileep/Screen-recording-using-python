import tkinter as tk
from tkinter import messagebox
import pyautogui
import cv2
import numpy as np
from PIL import Image, ImageTk
import threading
import time

class ScreenRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Recorder")
        self.root.geometry("300x150")

        self.recording = False
        self.video_writer = None
        self.thread = None

        self.start_button = tk.Button(root, text="Start Recording", command=self.start_recording)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.preview_label = tk.Label(root)
        self.preview_label.pack()

    def start_recording(self):
        self.recording = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        # Define the codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.video_writer = cv2.VideoWriter('output.avi', fourcc, 20.0, (1920, 1080))

        self.thread = threading.Thread(target=self.record_screen)
        self.thread.start()

    def stop_recording(self):
        self.recording = False
        self.thread.join()
        self.video_writer.release()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        messagebox.showinfo("Info", "Recording saved as output.avi")

    def record_screen(self):
        while self.recording:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            self.video_writer.write(frame)

            # Display the recording in the GUI
            frame = cv2.resize(frame, (320, 180))
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.preview_label.imgtk = imgtk
            self.preview_label.configure(image=imgtk)

            time.sleep(0.05)

if __name__ == "__main__":
    root = tk.Tk()
    recorder = ScreenRecorder(root)
    root.mainloop()