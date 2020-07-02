import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import os
import errno
import IPython.display as ipd

data_dir = "C:/Users/MADHUKAR/Desktop/ari.mp3"

access_rights = 0o777
output_dir = 'C:/Users/MADHUKAR/Desktop/graph'

try:
    os.makedirs(output_dir, access_rights, exist_ok=True)

except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    print("Creation of the directory %s failed" % output_dir)
    pass

else:
    print("Successfully created the directory %s" % output_dir)



y, sr = librosa.load(data_dir)
print(y)
librosa.feature.melspectrogram(y=y, sr=sr)
D = np.abs(librosa.stft(y))**2
S = librosa.feature.melspectrogram(S=D)
plt.figure(figsize=(10, 4))
librosa.display.specshow(librosa.power_to_db(S,ref=np.max),y_axis='mel', fmax=8000,x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel spectrogram')
plt.tight_layout()
plt.savefig(f'{output_dir}/Mel Spectrogram.png', format="PNG")
plt.show()
print('Mel Spectogram Plotted')
