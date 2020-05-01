# MFCC PLots


import librosa.display
import librosa as lr
import matplotlib.pyplot as plt
from glob import glob
import os
import errno

data_dir = "C:/Users/asus/Desktop/Song_test/Split/Done1.wav"
audio_files = glob(data_dir)
len(audio_files)

access_rights = 0o777
output_dir = 'C:/Users/asus/Desktop/Graph/Music/TestSubD1'

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

    librosa.feature.mfcc(y=y, sr=sr)
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
    librosa.feature.mfcc(S=librosa.power_to_db(S))

    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(mfccs, x_axis='time')
    plt.colorbar()
    plt.title('MFCC')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/Graph_{file}.png', format="PNG")
    plt.show()


print("Done Plotting MFCC")
