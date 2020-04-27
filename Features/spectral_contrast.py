import numpy as np
import os
import errno
import matplotlib.pyplot as plt
from glob import glob

import librosa.display

data_dir = 'C:/Users/MADHUKAR/Desktop/sample/*.wav'
audio_files = glob(data_dir)
len(audio_files)
output_dir = 'C:/Users/MADHUKAR/Desktop/graph'

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

    y, sr = librosa.load(audio_files[file])

    S = np.abs(librosa.stft(y))
    contrast = librosa.feature.spectral_contrast(S=S, sr=sr)

    plt.figure()
    plt.subplot(2, 1, 1)
    librosa.display.specshow(librosa.amplitude_to_db(S, ref = np.max), y_axis = 'log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Power spectrogram')
    plt.subplot(2, 1, 2)
    librosa.display.specshow(contrast, x_axis='time')
    plt.colorbar()
    plt.ylabel('Frequency bands')
    plt.title('Spectral contrast')
    plt.tight_layout()

    plt.savefig(f'{output_dir}/Graph_{file}.png', format="PNG")
    plt.show()