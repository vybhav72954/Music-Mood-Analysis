#Chroma Pitchclass
#Tonal Centroids


import librosa.display
import librosa as lr
import matplotlib.pyplot as plt
from glob import glob
import os
import errno

data_dir = "C:/Users/asus/Desktop/Song_test/Split/*.wav"
audio_files = glob(data_dir)
len(audio_files)

access_rights = 0o777
output_dir = 'C:/Users/asus/Desktop/Graph/Music/TestSubD1Tonal'
output_dir1 = 'C:/Users/asus/Desktop/Graph/Music/TestSubD1Chroma'

try:
    os.makedirs(output_dir, access_rights, exist_ok=True)

except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    print("Creation of the directory %s failed" % output_dir)
    pass

else:
    print("Successfully created the directory %s" % output_dir)

try:
    os.makedirs(output_dir1, access_rights, exist_ok=True)

except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    print("Creation of the directory %s failed" % output_dir1)
    pass

else:
    print("Successfully created the directory %s" % output_dir1)


for file in range(0, len(audio_files), 1):
    y, sr = librosa.load(audio_files[file])
    print(y)

    y = librosa.effects.harmonic(y)
    tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
    print(tonnetz)
    plt.subplot(2, 1, 1)
    librosa.display.specshow(tonnetz, y_axis='tonnetz')
    plt.colorbar()
    plt.title('Tonal Centroids (Tonnetz)')
    plt.savefig(f'{output_dir}/Graph_{file}.png', format="PNG")
    plt.show()

    librosa.display.specshow(librosa.feature.chroma_cqt(y, sr=sr), y_axis='chroma', x_axis='time')
    plt.colorbar()
    plt.title('Chroma')
    plt.tight_layout()
    plt.savefig(f'{output_dir1}/Graph_{file}.png', format="PNG")
    plt.show()

print('Tonal Centroids Done, Pitch Formatter  Done')

