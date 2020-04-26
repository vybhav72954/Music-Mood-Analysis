import librosa.display
import librosa
import matplotlib.pyplot as plt
import numpy as np

song="C:/Users/MADHUKAR/Desktop/Song_Data/2_Hello.wav"
y, sr = librosa.load(song, offset=30, duration=5)
print(y)

librosa.feature.rms(y=y)
S, phase = librosa.magphase(librosa.stft(y))
rms = librosa.feature.rms(S=S)


plt.figure()
plt.subplot(2, 1, 1)
plt.semilogy(rms.T, label='RMS Energy')

plt.xticks([])
plt.xlim([0, rms.shape[-1]])
plt.legend()
plt.subplot(2, 1, 2)
librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), y_axis='log', x_axis='time')
plt.title('log Power spectrogram')
plt.tight_layout()
plt.show()