import matplotlib.pyplot as plt
import librosa.display
import numpy as np
import IPython.display as ipd
import librosa
import matplotlib.pyplot as plt

song="C:/Users/MADHUKAR/Desktop/Song_Data/2_Hello.wav"
y, sr = librosa.load(song, offset=10, duration=15)
chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr, n_chroma=12, n_fft=4096)
chroma_cq = librosa.feature.chroma_cqt(y=y, sr=sr)
print(y)

librosa.display.specshow(librosa.feature.chroma_cqt(y, sr=sr), y_axis='chroma', x_axis='time')
plt.colorbar()
plt.title('Chroma')
plt.tight_layout()
plt.show()