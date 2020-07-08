
import wave

with wave.open ("filename.wav") as file: #Change the file name

    print (file.getparams())
