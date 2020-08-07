#TODO
'''
Add number of Features
Add types of Features
CSV Headers(if Possible)
'''


from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import MidTermFeatures

# mid term features saved in csv for each individual song file
MidTermFeatures.mid_feature_extraction_file_dir("D:/Capstone/Testing/New_directory",  1.0 , 0.75 , 0.050, 0.005,store_short_features=True, store_csv=True,plot=False )
# (folder_path, mid_window, mid_step,short_window, short_step,store_short_features=False, store_csv=False,plot=False):
