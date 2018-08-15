# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:00:52 2018

@author: appu
"""
#Importing Libraries
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

#Import Training and Testing Data set
training = pd.read_csv('Accident_train.csv')
testing = pd.read_csv('Accident_test.csv')

#Importing Collion Severity
y = training['Collision_Severity']
x = training.drop(['Collision_Ref_No','Weekday_of_Collision','Collision_Severity'], axis = 1)

#Applying Encoder to training data to transform the data into values
encoder = LabelEncoder()
mask = ~x['Policing_Area'].isnull()
x['Policing_Area'][mask] = encoder.fit_transform(x['Policing_Area'][mask])

#Applying Encoder to testing data to transform the data into values
k = testing['Collision_Severity']
l = testing.drop(['Collision_Ref_No','Weekday_of_Collision','Collision_Severity'], axis = 1)
encoder = LabelEncoder()
mask = ~l['Policing_Area'].isnull()
l['Policing_Area'][mask] = encoder.fit_transform(l['Policing_Area'][mask])

#Imputer modifies all the NA or missing values to NaN - training
imputer = Imputer(missing_values = 'NaN', strategy = 'most_frequent', axis = 1)
imputer = imputer.fit(x)
x = imputer.transform(x)

#Imputer modifies all the NA or missing values to NaN - testing
imputer = Imputer(missing_values = 'NaN', strategy = 'most_frequent', axis = 1)
imputer = imputer.fit(l)
l = imputer.transform(l)

#Random Forest Classifications
randFC = RandomForestClassifier(max_depth=6, n_estimators=10, max_features=1)

#Fitting variable into the classifier
randFC.fit(x,y)

#Splitting training data for validation
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=.33)
score = randFC.score(X_test, y_test)

#Print its score of testing data 
print(score)

#Results storing into varaiable
result = []
result = randFC.predict(l)

#Saving the file in csv format
l = []
for i in range(1,355):
    l.append(i)
df = pd.DataFrame(list(zip(l,result)), columns=["S.No.","Collision_Severity"])
df.to_csv('results.csv', index=False)
