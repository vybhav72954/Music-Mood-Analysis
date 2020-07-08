######TO BE CHECKED######




from pyAudioAnalysis import audioTrainTest as aT
from plotly import subplots
cm, thr_prre, pre, rec, thr_roc, fpr, tpr = aT.evaluate_model_for_folders(["C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 1/Agressive/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 1/Boisterous/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 1/Rowdy/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 1/Volatile/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 2/Confident/"
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 2/Fiery/"
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 2/Intense/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 2/Passionate/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 2/Rousing/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 3/Autumnal/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 3/Brooding/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 3/Literate/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 4/Bittersweet/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 4/Poignant/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 4/Wistful/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 5/Campy/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 5/whimsical/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 5/Wry/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 6/Cheerful/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 6/Rollicking/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 7/Fun/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 7/Humorous/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 7/Silly/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 7/Witty/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 8/Amiable-good natured/",
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 8/Sweet/"
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 9/Tense - Anxious/"
                               "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 9/Visceral/"], "C:/Users/asus/PycharmProjects/untitled/RF_Mirex","randomforest", "C:/Users/asus/Desktop/MIREX-like_mood/Audio/Cluster 1/Agressive/", plot=True)
