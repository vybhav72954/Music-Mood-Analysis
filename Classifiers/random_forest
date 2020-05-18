import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn import utils

df = pd.read_csv('C:/Users/MADHUKAR/Desktop/Capstone/samples/GTZAN.csv')
df['filename'].unique()

label_encoder = preprocessing.LabelEncoder()
df['filename']= label_encoder.fit_transform(df['filename'])
print(df['filename'].unique())

df['label']= label_encoder.fit_transform(df['label'])
print(df['label'].unique())

print(df)


X= df
y= df
X = X.astype(int)
y = y.astype(int)

clf = RandomForestClassifier(n_jobs=2, random_state=0)
clf.fit(X,y)
predictions = clf.predict(X)
print(accuracy_score(y,predictions))

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

random_forest = RandomForestClassifier(n_estimators=30, max_depth=10, random_state=1)

random_forest.fit(X_train, y_train)
y_predict = random_forest.predict(X_test)
accuracy_score(y_test, y_predict)
