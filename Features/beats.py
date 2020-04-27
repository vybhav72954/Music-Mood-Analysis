import numpy as np
import os
import errno
import matplotlib.pyplot as plt
from glob import glob
import librosa as lr
import librosa.display

data_dir = 'C:/Users/MADHUKAR/Desktop/sample/*.wav'
audio_files = glob(data_dir)
len(audio_files)
print(audio_files)
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
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

    onset_env = lr.onset.onset_strength(y, sr=sr, aggregate = np.median)
    tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env, sr = sr)

    hop_length = 512
    plt.figure(figsize=(8, 4))
    times = lr.times_like(onset_env, sr=sr, hop_length=hop_length)
    plt.plot(times, lr.util.normalize(onset_env), label = 'Onset strength')
    plt.vlines(times[beats], 0, 1, alpha=0.5, color='r', linestyle = '--', label = 'Beats')
    plt.legend(frameon=True, framealpha=0.75)

    plt.xlim(15, 30)
    plt.gca().xaxis.set_major_formatter(lr.display.TimeFormatter())
    plt.tight_layout()
    plt.savefig(f'{output_dir}/Graph_{file}.png', format="PNG")
    plt.show()

print("Done")