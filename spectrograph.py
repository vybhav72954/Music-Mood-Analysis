import matplotlib.pyplot as plt
import librosa.display
import numpy as np
import IPython.display as ipd
import librosa

song="C:/Users/MADHUKAR/Desktop/Song_Data/2_Hello.wav"

y, sr = librosa.load(song)
ipd.Audio(song)
print(y)

plt.figure(figsize=(50, 50))
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
plt.subplot(4, 2, 1)
librosa.display.specshow(D, y_axis='linear')
plt.colorbar(format='%+2.0f dB')
plt.title('Linear-frequency power spectrogram')
plt.show()
