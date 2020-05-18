from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures

[Fs, x] = audioBasicIO.read_audio_file("C:/Users/asus/Desktop/Test.wav")
Mono_Signal = audioBasicIO.stereo_to_mono(x)

[Feature, Feature_Names] = ShortTermFeatures.feature_extraction(Mono_Signal, Fs, 0.050 * Fs, 0.025 * Fs, deltas=True)
# print(Feature)
print (Feature_Names)
