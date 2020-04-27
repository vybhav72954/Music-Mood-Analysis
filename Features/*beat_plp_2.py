import numpy as np
import os
import errno
import matplotlib.pyplot as plt
from glob import glob
import scipy.stats
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

    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    pulse = librosa.beat.plp(onset_envelope=onset_env, sr=sr)

    tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env)
    beats_plp = np.flatnonzero(librosa.util.localmax(pulse))

    ax = plt.subplot(2, 1, 1)
    times = librosa.times_like(onset_env, sr=sr)
    plt.plot(times, librosa.util.normalize(onset_env), label = 'Onset strength')
    plt.vlines(times[beats], 0, 1, alpha=0.5, color='r',linestyle = '--', label = 'Beats')
    plt.legend(frameon=True, framealpha=0.75)
    plt.title('librosa.beat.beat_track')

    plt.subplot(2, 1, 2, sharex=ax)
    times = librosa.times_like(pulse, sr=sr)
    plt.plot(times, librosa.util.normalize(pulse),label = 'PLP')
    plt.vlines(times[beats_plp], 0, 1, alpha=0.5, color='r',linestyle = '--', label = 'PLP Beats')
    plt.legend(frameon=True, framealpha=0.75)
    plt.title('librosa.beat.plp')
    plt.xlim(30, 35)
    ax.xaxis.set_major_formatter(librosa.display.TimeFormatter())
    plt.tight_layout()

    plt.savefig(f'{output_dir}/Graph_{file}.png', format="PNG")
    plt.show()
