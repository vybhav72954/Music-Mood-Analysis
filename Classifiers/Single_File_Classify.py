from pyAudioAnalysis import audioTrainTest as aT

ID, Prob, Class = aT.file_classification("C:/Users/asus/Desktop/Test.wav", "C:/Users/asus/PycharmProjects/untitled/RF_Mirex", "randomforest")
print (ID)
print (Prob)
print (Class)
