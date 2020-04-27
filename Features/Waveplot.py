# Amplitude_Time Plots

import numpy as np
import os
import errno
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob

import librosa as lr

data_dir = 'C:/Users/asus/Desktop/Capstone_Code/Song_Data_1/*.wav'
audio_files = glob(data_dir)
len(audio_files)
output_dir = 'C:/Users/asus/Desktop/Graph/Music/TestSubD'

access_rights = 0o777

try:
    os.makedirs(output_dir, access_rights, exist_ok=True)
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    print("Creation of the directory %s failed" % output_dir)
    pass

else:
    print("Successfully created the directory %s" % output_dir)

for file in range(0, len(audio_files), 1):
    audio, sfreq = lr.load(audio_files[file], sr=None, mono=True, offset=0.0, duration=None)
    len(audio), sfreq
    Duration = len(audio)/sfreq
    print(Duration, " seconds")
    time = np.arange(0, len(audio)) / sfreq
    fig, ax = plt.subplots()
    ax.plot(time, audio)
    ax.set(xlabel='Time (s)', ylabel='Sound Amplitude')
    plt.savefig(f'{output_dir}/Graph_{file}.png', format="PNG")
    plt.show()
