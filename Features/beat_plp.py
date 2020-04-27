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

access_rights = 0o777
output_dir = 'C:/Users/MADHUKAR/Desktop/graph'

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

    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    pulse = librosa.beat.plp(onset_envelope=onset_env, sr=sr)

    prior = scipy.stats.lognorm(loc=np.log(120), scale=120, s=1)
    pulse_lognorm = librosa.beat.plp(onset_envelope=onset_env, sr=sr, prior = prior)
    melspec = librosa.feature.melspectrogram(y=y, sr=sr)

    ax = plt.subplot(3, 1, 1)
    librosa.display.specshow(librosa.power_to_db(melspec, ref=np.max), x_axis='time', y_axis='mel')

    plt.title('Mel spectrogram')
    plt.subplot(3, 1, 2, sharex=ax)
    plt.plot(librosa.times_like(onset_env), librosa.util.normalize(onset_env), label='Onset strength')
    plt.plot(librosa.times_like(pulse), librosa.util.normalize(pulse), label='Predominant local pulse (PLP)')
    plt.title('Uniform tempo prior [30, 300]')
    plt.subplot(3, 1, 3, sharex=ax)
    plt.plot(librosa.times_like(onset_env), librosa.util.normalize(onset_env), label='Onset strength')
    plt.plot(librosa.times_like(pulse_lognorm),librosa.util.normalize(pulse_lognorm), label='Predominant local pulse (PLP)')
    plt.title('Log-normal tempo prior, mean=120')
    plt.legend()
    plt.xlim([30, 35])
    plt.tight_layout()

    plt.savefig(f'{output_dir}/Graph_{file}.png', format="PNG")
    plt.show()
