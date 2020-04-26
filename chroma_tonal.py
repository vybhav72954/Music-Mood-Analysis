import matplotlib.pyplot as plt
import librosa.display
import numpy as np
import IPython.display as ipd
import librosa
import matplotlib.pyplot as plt

song="C:/Users/MADHUKAR/Desktop/Song_Data/2_Hello.wav"

y, sr = librosa.load(song)
print(y)

y = librosa.effects.harmonic(y)
tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
print(tonnetz)
plt.subplot(2, 1, 1)
librosa.display.specshow(tonnetz, y_axis='tonnetz')
plt.colorbar()
plt.title('Tonal Centroids (Tonnetz)')
plt.show()
librosa.display.specshow(librosa.feature.chroma_cqt(y, sr=sr), y_axis='chroma', x_axis='time')
plt.colorbar()
plt.title('Chroma')
plt.tight_layout()
plt.show()