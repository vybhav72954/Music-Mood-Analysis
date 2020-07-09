#MAKE A NEW DIRECTORY ANYWHERE, COPY THE PATH
#CHANGE THE PATH (OUTPUT DIRECTORY)
#RUN THE CODE
#DELETE ALL THE WAV FILES FROM THE SOURCE DIRECTORY
#COPY THE NEW FILES IN THE SOURCE (FROM DESTINATION)
#RUN THE BACTH COMMAND
#SEGREGATE FOLDERS INTO DIFFERENT CLUSTERS
import os
import soundfile

from glob import glob

import librosa as lr

data_dir = 'C:\\Users\\asus\\Desktop\\MIREX\\dataset\\Audio\\*.wav' #SOURCE

audio_files = glob(data_dir)
len(audio_files)


for file in range(0, len(audio_files), 1):
    audio, sfreq = lr.load(audio_files[file], sr=16000, mono=True)
    soundfile.write('C:\\Users\\asus\\Desktop\\MIREX\\dataset\\Audio_wav1\\%s.wav' % str(file+1).zfill(3), audio, 16000, subtype='PCM_24') #CHANGE THIS PATH
    print ('Done {}'.format(str(file)))
