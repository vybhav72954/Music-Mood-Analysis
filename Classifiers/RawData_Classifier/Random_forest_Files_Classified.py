from pyAudioAnalysis import audioTrainTest as aT
import os
import shutil


'''
# For Single File
class_id, probability, classes = aT.file_classification("D:\\Capstone\\Testing\\Single Song\\Passenger - Let Her Go 🎵.mp3",
                                                        "C:\\Users\\arman\\PycharmProjects\\Capstone\\Features\\RF_test", "randomforest")
print(class_id, probability, classes)
print(classes[int(class_id)])
'''

d = "D:\\Capstone\\Testing\\Single Song\\" # downsample done songs directory, I suggest make a new copy of that and then run
for path in os.listdir(d):
    source = os.path.join(d, path)
    #if os.path.isfile(source):
    print(source)

    class_id, probability, classes = aT.file_classification(source,
                                                            "C:\\Users\\arman\\PycharmProjects\\Capstone\\Features\\RF_test", "randomforest")

    print(class_id,classes)
    for count,name in enumerate(classes):
            if (count == int(class_id)):
                print(name) # PRINT OUT THE VALUE ACCORDING TO KEY
                output_dir = "D:\\Capstone\\Single Song\\" + name # make a new directory where songs in their emotions can be saved
                print(output_dir) # PRINT OUT THE DIRECTORY ACCORDING TO VALUE
                ################### EXCEPTION HANDLING ###############
                try:
                    os.makedirs(output_dir, 0o777, exist_ok=True)
                except OSError as exc:
                    if exc.errno != errno.EEXIST:
                        raise
                    print("Creation of the directory %s failed" % output_dir)
                    pass

                else:
                    print("Successfully created the directory %s" % output_dir)
                #output_dir = output_dir + "\\" + str(count) + ".wav" # to use in copyfile function
                shutil.move(source,output_dir)


