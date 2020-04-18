import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob

import librosa as lr

data_dir = 'C:/Users/asus/Desktop/genres/pop/*.wav'
audio_files = glob(data_dir)
len(audio_files)
output_dir= 'C:/Users/asus/Desktop/Graph/Pop'

for file in range(0, len(audio_files), 1):
    audio, sfreq = lr.load(audio_files[file])
    time = np.arange(0, len(audio)) / sfreq

    fig, ax = plt.subplots()
    ax.plot(time, audio)
    ax.set(xlabel='Time (s)', ylabel='Sound Amplitude')
    plt.savefig('Graph_{}.png'.format(file, output_dir), format="PNG")
    plt.show()