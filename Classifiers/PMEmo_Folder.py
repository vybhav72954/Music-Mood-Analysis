import pandas as pd
import os
import numpy as np

from pathlib import Path
from shutil import copy2

df = pd.read_csv('C:\\Users\\asus\\Documents\\Mood_Indexed.csv')

'''
for index, rows in df.iterrows():
    print (index, rows.song_Id, rows['name'])
    
    
    
    


df1 = df.sort_values(['name', 'song_Id'])
df1 = df1.drop(columns=['Arousal', 'Valence', 'closest_pairs', 'min_distance'])
#print (df1)
#df1 = df1.groupby(['name']).count()
directory = []
for index, rows in df1.iterrows():
    directory.append(rows['name'])
    #print(directory)

'''

# Path with extension-less files
source = Path("D:\\Study\\PMEmo2019\\Song")

for _, row in df.iterrows():
    # Convert to string and then create file path (without extension)
    filename = Path(str(row["song_Id"])).with_suffix(".wav")
    # Target folder path
    target = Path(row["name"])
    # Create folder
    target.mkdir(exist_ok=True)
    # Copy
    copy2(source / filename, target / filename)
