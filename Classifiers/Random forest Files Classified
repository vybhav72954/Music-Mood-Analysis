from pyAudioAnalysis import audioTrainTest as aT
import os
import shutil

d = "D:/Capstone/Testing/Single Song/"
for path in os.listdir(d):
    source = os.path.join(d, path)
    #if os.path.isfile(source):
    print(source)

    class_id, probability, classes = aT.file_classification(source,
                           "C:/Users/arman/PycharmProjects/Capstone/Features/RF_Mirex", "randomforest")

    print(class_id,classes)

    test_loc = {}
    test_loc[0] = 'Agressive'
    test_loc[1] = 'Boisterous'
    test_loc[2] = 'Rowdy'
    test_loc[3] = 'Volatile'
    test_loc[4] = 'Passionate'
    test_loc[5] = 'Rousing'
    test_loc[6] = 'Autumnal'
    test_loc[7] = 'Brooding'
    test_loc[8] = 'Literate'
    test_loc[9] = 'Bittersweet'
    test_loc[10] = 'Poignant'
    test_loc[11] = 'Wistful'
    test_loc[12] = 'Campy'
    test_loc[13] = 'Whimsical'
    test_loc[14] = 'Wry'
    test_loc[15] = 'Cheerful'
    test_loc[16] = 'Rollicking'
    test_loc[17] = 'Fun'
    test_loc[18] = 'Humorous'
    test_loc[19] = 'Silly'
    test_loc[20] = 'Witty'
    test_loc[21] = 'Amiable-good-natured'
    test_loc[22] = 'Sweet'
    test_loc[23] = 'Tense-Anxious'
    test_loc[24] = 'Visceral'
    for key in test_loc:
            if (key == class_id):
                print(test_loc[key]) # PRINT OUT THE VALUE ACCORDING TO KEY
                output_dir = "D:/Capstone/Testing/randomForest/" + test_loc[key]
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
                #output_dir = output_dir + "/" + str(count) + ".wav" # to use in copyfile function
                shutil.move(source,output_dir)

