from pyAudioAnalysis import audioTrainTest as aT
import os
import shutil

inp_dir = "D:/Capstone/Testing/Single Song/"
for path in os.listdir(inp_dir):
    source = os.path.join(inp_dir, path)
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
    test_loc[4] = 'Confident'
    test_loc[5] = 'Fiery'
    test_loc[6] = 'Intense'
    test_loc[7] = 'Passionate'
    test_loc[8] = 'Rousing'
    test_loc[9] = 'Autumnal'
    test_loc[10] = 'Brooding'
    test_loc[11] = 'Literate'
    test_loc[12] = 'Bittersweet'
    test_loc[13] = 'Poignant'
    test_loc[14] = 'Wistful'
    test_loc[15] = 'Campy'
    test_loc[16] = 'Whimsical'
    test_loc[17] = 'Wry'
    test_loc[18] = 'Cheerful'
    test_loc[19] = 'Rollicking'
    test_loc[20] = 'Fun'
    test_loc[21] = 'Humorous'
    test_loc[22] = 'Silly'
    test_loc[23] = 'Witty'
    test_loc[24] = 'Amiable-good-natured'
    test_loc[25] = 'Sweet'
    test_loc[26] = 'Tense-Anxious'
    test_loc[27] = 'Visceral'
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

