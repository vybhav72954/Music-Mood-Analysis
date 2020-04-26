import librosa.display
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