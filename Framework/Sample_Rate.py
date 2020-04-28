import numpy as np
import pandas as pd
import librosa as lr
import os
import errno
from glob import glob


access_rights = 0o777
output_dir = 'C:/Users/asus/Desktop/Graph/Capstone/CSV'
try:
    os.makedirs(output_dir, access_rights, exist_ok=True)

except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    print("Creation of the directory %s failed" % output_dir)
    pass

else:
    print("Successfully created the directory %s" % output_dir)

data_dir = "C:/Users/asus/Desktop/Capstone_Code/Song_Data/*.wav"
audio_files = glob(data_dir)

for file in range(0, len(audio_files), 1):
    print(lr.core.get_samplerate(audio_files[file]))
print('Done Sample Rate')

for file in range(0, len(audio_files), 1):

    y, sr = lr.load(audio_files[file], mono=True)
    print(sr)
print('Done Audio Input Array')
    
