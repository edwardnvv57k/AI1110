import numpy as np
from playsound import playsound
import time, pygame, random, os
from pygame import mixer
from tkinter import *
import tkinter as tk
from tkinter import Tk, ttk
import math

songnums = []

def Construct(songnums):
    while (len(songnums) != 20):
        a = math.ceil(np.random.uniform(0, 20))
        if a not in songnums:
            songnums.append(a)

bgcolor = "#BBFFFF"

class Playlist:

    def __init__(self, window):

        self.songnums= songnums
        self.window = window
        window.configure(bg = bgcolor)
        self.window.title("My Playlist")
        window.geometry('500x350')
        pygame.mixer.init()
        self.isPlaying = False

        self.Head = tk.Label(window, text="This Playlist is Randomly Generated", font = ("Rockwell", 22), bg = bgcolor, fg = "blue")
        self.Head.place(anchor = "center", relx = 0.5, rely = 0.13)
        
        self.button = tk.Button(window, text="Start / Next", height = 2, width = 12, command=self.playsong, font = ("Rockwell", 15))
        self.button.place(anchor = "center", relx = 0.5, rely = 0.4)

        self.button = tk.Button(window, text="Pause / Resume", height = 2, width = 12, command=self.pause_resume, font = ("Rockwell", 15))
        self.button.place(anchor = "center", relx = 0.5, rely = 0.6)

    def playsong(self):

        pygame.mixer.music.stop()

        self.NP = tk.Label(root, text="Now playing:  ", font = ("Rockwell", 20), bg = bgcolor, fg = "blue")
        self.NP.place(anchor = "se", relx = 0.75, rely = 0.9)

        if (len(songnums) == 0):
            Construct(songnums)

        songname = str(self.songnums.pop()) + ".mp3"

        pygame.mixer.music.load("Music/" + songname)
        pygame.mixer.music.play()
        nowplaying = tk.Label(root,text = "  " + songname, font = ("Rockwell", 20), bg = bgcolor, fg = "blue")
        nowplaying.place(anchor = "se", relx = 0.9, rely = 0.9)

        print(songname)
        self.isPlaying = True
        self.window.after(20, self.autoplay)

    def autoplay(self):

        if not pygame.mixer.music.get_busy() and self.isPlaying:
            self.playsong()
        else:
            self.window.after(20, self.autoplay)
    
    def pause_resume(self):

        if self.isPlaying:
            pygame.mixer.music.pause()
            self.isPlaying = False
        else:
            pygame.mixer.music.unpause()
            self.isPlaying = True
            

root = tk.Tk()
MyPlaylist = Playlist(root)
root.mainloop()
