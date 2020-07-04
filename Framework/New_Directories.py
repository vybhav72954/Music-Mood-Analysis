from random import seed #Not Needed in Classification
from random import randint #Not Needed in Classification
import os
access_rights = 0o777
######### DICTIONARY #######################
test_loc = {} 
test_loc[1] = 'Vybhav'
test_loc[2] = 'Arman'
test_loc[3] = 'Vedansh'
test_loc[4] = 'Naruto'
test_loc[5] = 'Ichigo'
test_loc[6] = 'Goku'
test_loc[7] = 'Astrian'
test_loc[8] = 'PUBG'
test_loc[9] = 'Why'

########GENERATING A RANDOM INTEGER< NOT NEEDED #########
print (test_loc)
seed(1)
for _ in range (5):
    value = randint(1, 10)
    print(value)
    ########## ITERATING THRUGH DICT USING KEYS #########
    for key in test_loc:
        if (key == value):
            print (test_loc[key]) # PRINT OUT THE VALUE ACCORDING TO KEY
            output_dir = "C:/Users/asus/Desktop/Arman/" + test_loc[key]
            print (output_dir) # PRINT OUT THE DIRECTORY ACCORDING TO VALUE
            ################### EXCEPTION HANDLING ###############
            try:
                os.makedirs(output_dir, access_rights, exist_ok=True)
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
                print("Creation of the directory %s failed" % output_dir)
                pass

            else:
                print("Successfully created the directory %s" % output_dir)
