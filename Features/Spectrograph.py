# Spectogram


import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import os
import errno
import IPython.display as ipd

data_dir = "C:/Users/asus/Desktop/Song_test/Split/*.wav"
audio_files = glob(data_dir)
len(audio_files)

access_rights = 0o777
output_dir = 'C:/Users/asus/Desktop/Graph/Music/TestSubD2Spec'

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
    y, sr = librosa.load(audio_files[file])
    print(y)
    ipd.Audio(audio_files[file])

    plt.figure(figsize=(50, 50))
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    plt.subplot(4, 2, 1)
    librosa.display.specshow(D, y_axis='linear')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Linear-frequency power spectrogram')
    plt.show()


print('Spectogram Plotted')
