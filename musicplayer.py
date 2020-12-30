import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

# creating window interface for the player
musicplayer = tkr.Tk();

# adding the title of the interface
musicplayer.title("Music Player")

# selecting dimentions of the window
musicplayer.geometry("450x350")

# asking for music directory
directory = askdirectory();

# setting music directory to the current working directory
os.chdir(directory)

# creating songlist
songlist = os.listdir()

# creating playlist
playlist = tkr.Listbox(musicplayer, font="Cambria 14 bold", bg="cyan2", selectmode=tkr.SINGLE)

# adding songs from songlist
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

# initializing modules
pygame.init()
pygame.mixer.init()


# play function
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()


# stop function
def stop():
    pygame.mixer.music.stop()


# pause function
def pause():
    pygame.mixer.music.pause()


# resume function
def resume():
    pygame.mixer.music.unpause()


# creating buttons
button_play = tkr.Button(musicplayer, height=3, width=10, text="Play", font="Cambria 14 bold", command=play,
                         bg="lime green", fg="black")
button_stop = tkr.Button(musicplayer, height=3, width=10, text="Stop", font="Cambria 14 bold", command=stop,
                         bg="red", fg="black")
button_pause = tkr.Button(musicplayer, height=3, width=10, text="Pause", font="Cambria 14 bold", command=pause,
                          bg="yellow", fg="black")
button_resume = tkr.Button(musicplayer, height=3, width=10, text="Resume", font="Cambria 14 bold", command=resume,
                           bg="blue", fg="black")

var = tkr.StringVar()
song_title = tkr.Label(musicplayer, font="Cambria 12 bold", textvariable=var)
song_title.pack()

button_play.pack()
button_stop.pack()
button_pause.pack()
button_resume.pack()

playlist.pack(fill="both", expand="yes")

musicplayer.mainloop()
