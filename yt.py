from pytube import YouTube
from time import sleep
from tqdm import tqdm
import os
from moviepy.editor import *

url = input("Enter video URL ")

yt = YouTube(url)
print("Downloading " + yt.title)
print("1. Download video and audio")
print("\n 2. Download audio only")
    
def mp4convert(mp4,mp3):
    mp4_source = AudioFileClip(mp4)
    mp4_source.write_audiofile(mp3)
    mp4_source.close()

def downloadVideo():
    vid = yt.streams.get_highest_resolution()
    vid.download()
    print("Download complete")

def downloadAudio():
    audio = yt.streams.get_by_itag(140)
    audio.download()
    old = yt.title + '.mp4'
    new = yt.title + '.mp3'
    mp4convert(old, new)
    os.remove(old)
    print("Download complete")

selection = input("Select: ")
if selection == "1":
    downloadVideo()
if selection == "2":
    downloadAudio()



