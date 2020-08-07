from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures
from pyAudioAnalysis import MidTermFeatures

[Fs, x] = audioBasicIO.read_audio_file("C:/Users/arman/Desktop/test.wav")
Mono_Signal = audioBasicIO.stereo_to_mono(x)

#short term features
[Feature, Feature_Names] = ShortTermFeatures.feature_extraction(Mono_Signal, Fs, 0.050 * Fs, 0.025 * Fs, deltas=True)
print (Feature_Names)

#mid term features
[mid_features, short_features, mid_feature_names] = MidTermFeatures.mid_feature_extraction(Mono_Signal, Fs, 1.0 * Fs, 0.75 * Fs, 0.050 * Fs, 0.005 * Fs)
#mid_feature_extraction(signal, sampling_rate, mid_window, mid_step, short_window, short_step)
print(mid_features, short_features, mid_feature_names)
