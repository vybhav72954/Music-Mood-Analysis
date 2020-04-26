import librosa.display
import librosa
import matplotlib.pyplot as plt

song="C:/Users/MADHUKAR/Desktop/Song_Data/2_Hello.wav"
y, sr = librosa.load(song, offset=30, duration=5)
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
plt.show()