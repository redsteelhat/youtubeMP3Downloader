from pytube import YouTube
import os

link = input("Enter the link of the video you want to download: ")
router = input("Enter the name of output directory: ")

try:
    yt = YouTube(link)
except:
    print("Link is not valid!")
    exit()

mp3 = yt.streams.filter(only_audio=True).first()

print("Loading...")
output = mp3.download(router)

base, ext = os.path.splitext(output)
to_mp3 = base + ".mp3"
os.rename(output, to_mp3)

print("Upload complete." + '✓')