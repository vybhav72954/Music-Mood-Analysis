# READ THE INSTRUCTIONS
# This is Specifically designed for GTZAN Database
# Will revise it by 2nd May
# Then Only can be used for other Directories
# Only works on preprocessed DATA (IMPORTANT)
# Download TensorFlow and Keras before anything (Use YT Videos)

import librosa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
import csv

#   from sklearn.model_selection import train_test_split
#   from sklearn.preprocessing import LabelEncoder, StandardScaler

header = 'filename chroma_stft rmse spectral_centroid spectral_bandwidth rolloff zero_crossing_rate'
for i in range(1, 21):
    header += f' mfcc{i}'
header += ' label'
header = header.split()

file = open('C:/Users/asus/Desktop/GTZAN.csv', 'w', newline='') # Where you want to save the file
with file:
    writer = csv.writer(file)
    writer.writerow(header)
genres = 'blues classical country disco hiphop jazz metal pop reggae rock'.split()
for g in genres:
    for filename in os.listdir(f'C:/Users/asus/Desktop/GTZAN/{g}'): # Where is the Database Direcory
        songname = f'C:/Users/asus/Desktop/GTZAN/{g}/{filename}' # Where are the Songs
        y, sr = librosa.load(songname, mono=True, duration=30)
        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        rmse = librosa.feature.rms(y=y)
        spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        zcr = librosa.feature.zero_crossing_rate(y)
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        to_append = f'{filename} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'
        for e in mfcc:
            to_append += f' {np.mean(e)}'
        to_append += f' {g}'
        file = open('data.csv', 'a', newline='')
        with file:
            writer = csv.writer(file)
            writer.writerow(to_append.split())
