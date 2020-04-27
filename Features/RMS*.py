# RMS Energy


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
    y, sr = librosa.load(audio_files[file])

    print(y)

    librosa.feature.rms(y=y)
    S, phase = librosa.magphase(librosa.stft(y))
    rms = librosa.feature.rms(S=S)

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.semilogy(rms.T, label='RMS Energy')

    plt.xticks([])
    plt.xlim([0, rms.shape[-1]])
    plt.legend()
    plt.subplot(2, 1, 2)
    librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), y_axis='log', x_axis='time')
    plt.title('log Power spectrogram')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/Graph_{file}.png', format="PNG")
    plt.show()

print('RMS Done')

