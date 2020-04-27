import os
import errno

access_rights = 0o777 # Access right, determines the pemission i.e. read, write etc

output_dir = 'C:/Users/asus/Desktop/Graph/Music/TestSubD' #Directory's path

try:
    os.makedirs(output_dir, access_rights, exist_ok=True)
    
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    print("Creation of the directory %s failed" % output_dir)
    pass

else:
    print("Successfully created the directory %s" % output_dir)
#  plt.savefig(f'{output_dir}/Graph_{file}.png', format="PNG")
#  This Fumction is needed plt.show() to save files in the output_dir
