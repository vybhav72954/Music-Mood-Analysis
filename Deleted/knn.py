from pyAudioAnalysis import audioTrainTest as aT


paths = ['C:/Users/MADHUKAR/Desktop/Capstone/samples/GTZAN/blues']

fs=44100

mid_window = fs
mid_step = 0.5 * fs
short_window = 0.050 * fs
short_step = 0.025 * fs
classifier_type = "knn"
model_name = "knn_train"

aT.extract_features_and_train(paths, mid_window, mid_step, short_window, short_step, classifier_type, model_name,
                              compute_beat=False, train_percentage=0.90)
