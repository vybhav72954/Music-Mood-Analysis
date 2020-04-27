# Chromagram STFT


import librosa.display
import librosa
import matplotlib.pyplot as plt
import numpy as np
import os
import errno
from glob import glob

song_dir = 'C:/Users/MADHUKAR/Desktop/sample/*.wav'

print(song_dir)
song = glob(song_dir)
print(song)

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

for song in song:
  i=1

  y, sr = librosa.load(song, offset=30, duration=5)
  print(y)

  S = np.abs(librosa.stft(y))
  chroma = librosa.feature.chroma_stft(S=S, sr=sr)
  print(chroma)

  plt.figure(figsize=(10, 4))
  librosa.display.specshow(chroma, y_axis='chroma', x_axis='time')
  plt.colorbar()
  plt.title('Chromagram')
  plt.tight_layout()
  plt.savefig(f'{output_dir}/Graph_{i}.png', format="PNG")
  plt.show()
  i=i+1

print("Done")
