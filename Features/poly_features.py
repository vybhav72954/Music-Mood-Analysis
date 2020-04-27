import numpy as np
import os
import errno
import matplotlib.pyplot as plt
from glob import glob
import librosa
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
    p0 = librosa.feature.poly_features(S=S, order=0)
    p1 = librosa.feature.poly_features(S=S, order=1)
    p2 = librosa.feature.poly_features(S=S, order=2)

    plt.figure(figsize=(8, 8))
    ax = plt.subplot(4, 1, 1)
    plt.plot(p2[2], label='order=2', alpha=0.8)
    plt.plot(p1[1], label='order=1', alpha=0.8)
    plt.plot(p0[0], label='order=0', alpha=0.8)
    plt.xticks([])
    plt.ylabel('Constant')
    plt.legend()
    plt.subplot(4, 1, 2, sharex=ax)
    plt.plot(p2[1], label='order=2', alpha=0.8)
    plt.plot(p1[0], label='order=1', alpha=0.8)
    plt.xticks([])
    plt.ylabel('Linear')
    plt.subplot(4, 1, 3, sharex=ax)
    plt.plot(p2[0], label='order=2', alpha=0.8)
    plt.xticks([])
    plt.ylabel('Quadratic')
    plt.subplot(4, 1, 4, sharex=ax)
    librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), y_axis = 'log')
    plt.tight_layout()

    plt.savefig(f'{output_dir}/Graph_{file}.png', format="PNG")

    plt.show()