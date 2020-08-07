from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures

#TODO
'''
Add number of Features
Add types of Features
'''
from glob import glob

data_dir = "C:/Users/MADHUKAR/Desktop/test/abc/*.wav"          #Path to sample directory
audio_files = glob(data_dir)

for filename in range(0, len(audio_files), 1): 
    [Fs, x] = audioBasicIO.read_audio_file(audio_files[filename])     #Reading indiviudal songs 
    Mono_Signal = audioBasicIO.stereo_to_mono(x)
    print(Fs)

    [Feature, Feature_Names] = ShortTermFeatures.feature_extraction(Mono_Signal, Fs, 0.050 * Fs, 0.025 * Fs, deltas=True) #Song feature extraction
    print(Feature)
