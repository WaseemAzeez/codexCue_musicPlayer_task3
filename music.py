import os
import pygame
from tkinter import Tk, Button, filedialog

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        self.master.geometry("300x100")

        self.load_button = Button(master, text="Load Music", command=self.load_music)
        self.play_button = Button(master, text="Play", command=self.play_music)
        self.pause_button = Button(master, text="Pause", command=self.pause_music)
        self.stop_button = Button(master, text="Stop", command=self.stop_music)

        self.load_button.pack()
        self.play_button.pack()
        self.pause_button.pack()
        self.stop_button.pack()

        self.music_loaded = False
        self.music_playing = False
        self.music_paused = False

    def load_music(self):
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Music",
                                              filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*")))
        if filename:
            pygame.mixer.init()
            pygame.mixer.music.load(filename)
            self.music_loaded = True

    def play_music(self):
        if self.music_loaded and not self.music_playing:
            pygame.mixer.music.play()
            self.music_playing = True

    def pause_music(self):
        if self.music_playing and not self.music_paused:
            pygame.mixer.music.pause()
            self.music_paused = True

    def stop_music(self):
        if self.music_playing or self.music_paused:
            pygame.mixer.music.stop()
            self.music_playing = False
            self.music_paused = False


def main():
    root = Tk()
    music_player = MusicPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
