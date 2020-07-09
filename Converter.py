# FOLLOW THESE INSTRUCTIONS CAREFULLY
# 
# THIS WILL COME HANDY LATER ON
import os
from glob import glob

import pydub

song_dir = 'C:\\Users\\asus\\Desktop\\MIREX\\dataset\\Audio\\*.mp3'  # Directory of File (Extension is acc. to file being converted
# If mp3 file ko wav me convert kr rhe, put mp3 here
print(song_dir)
song = glob(song_dir)  # Glob for pattern
print(song)
for song in song:
    mp3_song = os.path.splitext(song)[0] + '.wav'  # Changing the extension to the target file type
    sound = pydub.AudioSegment.from_mp3(song)
    sound.export(mp3_song, format="wav")  # Actual Conversion yha pr h using PyDub
    os.remove(song)
print("Conversion Done")
