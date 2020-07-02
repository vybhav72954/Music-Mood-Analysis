import numpy as np
import os
import errno
import matplotlib.pyplot as plt
from glob import glob

import librosa.display

data_dir = 'C:/Users/MADHUKAR/Desktop/ari.mp3'

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



y, sr = librosa.load(data_dir, offset = 10, duration = 15)

chroma_cens = librosa.feature.chroma_cens(y=y, sr=sr)
chroma_cq = librosa.feature.chroma_cqt(y=y, sr=sr)

plt.figure()
plt.subplot(2, 1, 1)
librosa.display.specshow(chroma_cq, y_axis='chroma')
plt.title('chroma_cq')
plt.colorbar()
plt.subplot(2, 1, 2)
librosa.display.specshow(chroma_cens, y_axis='chroma', x_axis='time')
plt.title('chroma_cens')
plt.colorbar()
plt.tight_layout()

plt.savefig(f'{output_dir}/Chroma_Cens.png', format="PNG")
plt.show()
