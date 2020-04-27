import numpy as np
import os
import errno
import matplotlib.pyplot as plt
from glob import glob
import librosa
import scipy.stats

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
    onset_env = librosa.onset.onset_strength(y, sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)

    tempo = tempo.item()
    prior = scipy.stats.uniform(30, 300)  # uniform over 30-300 BPM
    utempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr, prior=prior)
    utempo = utempo.item()

    hop_length = 512
    ac = librosa.autocorrelate(onset_env, 2 * sr // hop_length)
    freqs = librosa.tempo_frequencies(len(ac), sr=sr, hop_length = hop_length)

    plt.figure(figsize=(8, 4))
    plt.semilogx(freqs[1:], librosa.util.normalize(ac)[1:], label = 'Onset autocorrelation', basex = 2)
    plt.axvline(tempo, 0, 1, color='r', alpha=0.75, linestyle='--', label = 'Tempo (default prior): {:.2f} BPM'.format(tempo))
    plt.axvline(utempo, 0, 1, color='y', alpha=0.75, linestyle=':', label = 'Tempo (uniform prior): {:.2f} BPM'.format(utempo))
    plt.xlabel('Tempo (BPM)')
    plt.grid()
    plt.title('Static tempo estimation')
    plt.legend(frameon=True)
    plt.axis('tight')

    plt.savefig(f'{output_dir}/Graph_{file}.png', format="PNG")
    plt.show()


