# Constant Power chroma


import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import os
import errno
import IPython.display as ipd

data_dir = 'C:/Users/asus/Desktop/Capstone_Code/Song_Data_1/*.wav'
audio_files = glob(data_dir)
len(audio_files)
print(audio_files)
access_rights = 0o777
output_dir = 'C:/Users/asus/Desktop/Graph/Music/TestSubD2Spec/d3'

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
    y, sr = librosa.load(audio_files[file], offset=10, duration=15)
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr, n_chroma=12, n_fft=4096)
    chroma_cq = librosa.feature.chroma_cqt(y=y, sr=sr)
    print(y)

    librosa.display.specshow(librosa.feature.chroma_cqt(y, sr=sr), y_axis='chroma', x_axis='time')
    plt.colorbar()
    plt.title('Chroma')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/Graph_{file}.png', format="PNG")
    plt.show()
    print(y)
    ipd.Audio(audio_files[file])

print('Chroma Constant Power Plotted')
