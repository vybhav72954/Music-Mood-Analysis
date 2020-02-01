# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob 

import librosa as lr

data_dir = './Desktop/mysongs' 
audio_files = glob(data_dir + '/*.wav')

audio,sfreq = lr.load(audio_files[0])
time = np.arange(0, len(audio))/sfreq

fig, ax = plt.subplots()
ax.plot(time, audio)
ax.set(xlabel='Time (s)', ylabel='Sound Amplitude') 
plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob 

import librosa as lr

data_dir = './Desktop/mysongs' 
audio_files = glob(data_dir + '/*.wav')

audio,sfreq = lr.load(audio_files[0])
time = np.arange(0, len(audio))/sfreq

fig, ax = plt.subplots()
ax.plot(time, audio)
ax.set(xlabel='Time (s)', ylabel='Sound Amplitude') 
plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob 

import librosa as lr

data_dir = './Desktop/wav files' 
audio_files = glob(data_dir + '/*.wav')

for file in range(0, len(audio_files), 1):
    audio,sfreq = lr.load(audio_files[file])
    time = np.arange(0, len(audio))/sfreq
    
    fig, ax = plt.subplots()
    ax.plot(time, audio)
    ax.set(xlabel='Time (s)', ylabel='Sound Amplitude') 
    plt.show()
