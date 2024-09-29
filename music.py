import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Function to load a music file
def load_music():
    file_path = filedialog.askopenfilename(filetypes=[("Music Files", "*.mp3 *.wav")])
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        # Update the status label to show the loaded file
        status_label.config(text=f"Playing: {file_path.split('/')[-1]}")

# Function to play the music (resume)
def play_music():
    pygame.mixer.music.unpause()
    # Update the status label to show music is resumed
    status_label.config(text="Music Resumed")

# Function to pause the music
def pause_music():
    pygame.mixer.music.pause()
    # Update the status label to show music is paused
    status_label.config(text="Music Paused")

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()
    # Update the status label to show music is stopped
    status_label.config(text="Music Stopped")

# Initialize the main window
root = tk.Tk()
root.title("Simple Music Player")

# Set window size
root.geometry("300x200")

# Create buttons for the music player
load_button = tk.Button(root, text="Load Music", command=load_music, width=25)
play_button = tk.Button(root, text="Play", command=play_music, width=25)
pause_button = tk.Button(root, text="Pause", command=pause_music, width=25)
stop_button = tk.Button(root, text="Stop", command=stop_music, width=25)

# Arrange buttons in the window
load_button.pack(pady=5)
play_button.pack(pady=5)
pause_button.pack(pady=5)
stop_button.pack(pady=5)

# Label to show the status of the music player
status_label = tk.Label(root, text="No Music Loaded", relief=tk.SUNKEN, anchor=tk.W)
status_label.pack(fill=tk.X, pady=10)

# Run the application
root.mainloop()
