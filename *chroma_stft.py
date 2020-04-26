import librosa.display
import librosa
import matplotlib.pyplot as plt
import numpy as np

song="C:/Users/MADHUKAR/Desktop/Song_Data/2_Hello.wav"
y, sr = librosa.load(song, offset=30, duration=5)
print(y)

y, sr = librosa.load(librosa.util.example_audio_file())
librosa.feature.chroma_stft(y=y, sr=sr)

S = np.abs(librosa.stft(y))
chroma = librosa.feature.chroma_stft(S=S, sr=sr)
print(chroma)

plt.figure(figsize=(10, 4))
librosa.display.specshow(chroma, y_axis='chroma', x_axis='time')
plt.colorbar()
plt.title('Chromagram')
plt.tight_layout()
plt.show()
