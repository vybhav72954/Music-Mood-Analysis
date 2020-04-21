# FOLLOW THESE INSTRUCTIONS CAREFULLY
# COPY ALL THE SONGS IN A NEW DIRECTORY CALLED "Song_Data", KEEP BOTH THE DIRECTORIES
# YOU WIILL HAVE TO CAHNGE USER IN THE PATH, e.g. MY USER IS ASUS, DO THE CAHNGES ACCORDINGLY
# I SUGGEST YOU MAKE A SEPARATE DIRECTORY FOR CODE AND RESULTS, <YOUR WISH>
# DO NECCESSARY CHANGES IN "song_dir" variable
# I REPEAT COPY THE SONGS AND KEEP BOTH THE DIRECTORIES
# THIS WILL COME HANDY LATER ON
import os
from glob import glob

import pydub

song_dir = 'C:/Users/asus/Desktop/Capstone_Code/Song_Data/*.mp3'  # Directory of File (Extension is acc. to file being converted
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
