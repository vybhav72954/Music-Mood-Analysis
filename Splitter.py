#  import os
#  from glob import glob

from pydub import AudioSegment
#  t1 = t1 * 1000
#  t2 = t2 * 1000
newAudio = AudioSegment.from_mp3("C:/Users/asus/Desktop/Song_test/Can't Help_WAV_1.mp3")
thirty_seconds = 30 * 1000
first_thirty = newAudio[:thirty_seconds]
Next_thirty = newAudio[30 * 1000: thirty_seconds]
#  newAudio = newAudio[t1:t2]
#  newAudio.export('newSong.wav', format="wav")
first_thirty.export('Cant help_first30.wav', format="mp3")
Next_thirty.export('Cant help_next30.wav', format="mp3")
print("Done")
