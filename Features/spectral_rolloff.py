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

    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    S, phase = librosa.magphase(librosa.stft(y))

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.semilogy(rolloff.T, label='Roll-off frequency')
    plt.ylabel('Hz')
    plt.xticks([])
    plt.xlim([0, rolloff.shape[-1]])
    plt.legend()
    plt.subplot(2, 1, 2)
    librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), y_axis = 'log', x_axis = 'time')
    plt.title('log Power spectrogram')
    plt.tight_layout()

    plt.savefig(f'{output_dir}/Graph_{file}.png', format="PNG")
    plt.show()