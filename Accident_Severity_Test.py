# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:59:09 2018

@author: appu
"""
import pandas as pd
from sklearn.preprocessing import Imputer, Normalizer, StandardScaler
from sklearn.preprocessing import LabelEncoder, LabelBinarizer
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
import numpy as np

data = pd.read_csv('Accident_train.csv')
test = pd.read_csv('Accident_test.csv')

y = data['Collision_Severity']
x = data.drop(['Collision_Ref_No','Policing_Area','Collision_Severity','Ped_Crossing_HC','Weekday_of_Collision','Day_of_Collision','Month_of_Collision','Hour_of_Collision','Special_Conditions_at_Site'], axis = 1)

k = test['Collision_Severity']
l = test.drop(['Collision_Ref_No','Policing_Area','Collision_Severity','Ped_Crossing_HC','Weekday_of_Collision','Day_of_Collision','Month_of_Collision','Hour_of_Collision','Special_Conditions_at_Site'], axis = 1)

imputer = Imputer(missing_values = 'NaN', strategy = 'most_frequent', axis = 1)
imputer = imputer.fit(x)
x = imputer.transform(x)


imputer = Imputer(missing_values = 'NaN', strategy = 'most_frequent', axis = 1)
imputer = imputer.fit(l)
l = imputer.transform(l)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=.20, stratify = y)

learning_rates = [0.05, 0.1, 0.15, 0.25, 0.5, 0.75, 1]
for learning_rate in learning_rates:
    clf = GradientBoostingClassifier(learning_rate = learning_rate, n_estimators= 70, max_depth=3, min_samples_split=20, min_samples_leaf = 1, subsample =1, max_features = 'auto', random_state = 42)
    clf.fit(X_train,y_train)
    print("Learning rate: ", learning_rate)
    print("Accuracy score (training): {0:.3f}".format(clf.score(X_train, y_train)))
    print("Accuracy score (validation): {0:.3f}".format(clf.score(X_test, y_test)))
    print()
    
    
