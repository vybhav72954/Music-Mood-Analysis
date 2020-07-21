import pandas as pd
import numpy as np
import csv

mood = pd.read_csv("C:/Users/asus/Desktop/Mood_Coordinates.csv")
song_value = pd.read_csv("C:/Users/asus/Desktop/Harmonic_AV_test.csv")

df_temp = mood.loc[:, ['Arousal','Valence']]
#print (song_value)
df_temp1 = song_value.loc[:, ['Arousal','Valence']]
#print (df_temp1)
df_n1 = mood.loc[:, ['Arousal','Valence']].to_numpy()
df_n2 = song_value.loc[:, ['Arousal','Valence']].to_numpy()

'''
for x,y in df_n2:
    for a,b in df_n1:
        np.linalg.norm(df_n2[x][y] - df_n1[a][b])
'''

import scipy
from scipy import spatial
ary = scipy.spatial.distance.cdist(mood.loc[:, ['Arousal','Valence']], song_value.loc[:, ['Arousal','Valence']], metric='euclidean')
#print (ary)
euclid = pd.DataFrame(ary)
#print (euclid)
