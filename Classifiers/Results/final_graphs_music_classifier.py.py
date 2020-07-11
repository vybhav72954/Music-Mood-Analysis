#CHECKED 

from pyAudioAnalysis import audioTrainTest as aT
from plotly import subplots
cm, thr_prre, pre, rec, thr_roc, fpr, tpr = aT.evaluate_model_for_folders(["D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 1\\Agressive\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 1\\Boisterous\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 1\\Rowdy\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 1\\Volatile\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 2\\Confident\\"
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 2\\Fiery\\"
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 2\\Intense\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 2\\Passionate\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 2\\Rousing\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 3\\Autumnal\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 3\\Brooding\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 3\\Literate\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 4\\Bittersweet\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 4\\Poignant\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 4\\Wistful\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 5\\Campy\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 5\\whimsical\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 5\\Wry\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 6\\Cheerful\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 6\\Rollicking\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 7\\Fun\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 7\\Humorous\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 7\\Silly\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 7\\Witty\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 8\\Amiable-good natured\\",
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 8\\Sweet\\"
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 9\\Tense - Anxious\\"
                                                                           "D:\\Capstone\\MIREX-like_mood\\dataset\\Audio\\Cluster 9\\Visceral\\"],
                                                                           "C:\\Users\\arman\\PycharmProjects\\Capstone\\Features\\RF1", "randomforest", "Agressive", plot=True)
