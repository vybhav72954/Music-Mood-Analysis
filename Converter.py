import os
import pydub
from glob import glob

song_dir = 'C:/Users/asus/Desktop/Song_test/*wav'  # Directory of File (Extension is acc. to the file to be converted
song = glob(song_dir)  # Glob for pattern
print(song)
for song in song:
    mp3_song = os.path.splitext(song)[0] + '.mp3'  # Changing the extension to the target file type
    sound = pydub.AudioSegment.from_mp3(song)
    sound.export(mp3_song, format="mp3")   # Actual Conversion yha pr h using PyDub
print("Conversion Done")
