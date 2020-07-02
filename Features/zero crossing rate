import librosa.display
import librosa
import matplotlib.pyplot as plt
import os
import errno
from glob import glob

song_dir = 'C:/Users/MADHUKAR/Desktop/ari.mp3'

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


y, sr = librosa.load(song_dir)
librosa.feature.zero_crossing_rate(y)


print("Done")

y, sr = librosa.load(librosa.util.example_audio_file())
zcr = librosa.feature.zero_crossing_rate(y)
print(zcr)
