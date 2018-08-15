from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

data = pd.read_csv('Accident_train.csv')
test = pd.read_csv('Accident_test.csv')

data.head()

y = data['Collision_Severity']
x = data.drop(['Collision_Ref_No','Weekday_of_Collision','Collision_Severity'], axis = 1)
encoder = LabelEncoder()
mask = ~x['Policing_Area'].isnull()
x['Policing_Area'][mask] = encoder.fit_transform(x['Policing_Area'][mask])
'''

k = test['Collision_Severity']
l = test.drop(['Collision_Ref_No','Weekday_of_Collision','Collision_Severity'], axis = 1)
encoder = LabelEncoder()
mask = ~l['Policing_Area'].isnull()
l['Policing_Area'][mask] = encoder.fit_transform(l['Policing_Area'][mask])
'''
y = data['Collision_Severity']
x = data.drop(['Collision_Ref_No','Policing_Area','Collision_Severity','Ped_Crossing_HC','Weekday_of_Collision','Day_of_Collision','Month_of_Collision','Hour_of_Collision','Special_Conditions_at_Site'], axis = 1)

k = test['Collision_Severity']
l = test.drop(['Collision_Ref_No','Policing_Area','Collision_Severity','Ped_Crossing_HC','Weekday_of_Collision','Day_of_Collision','Month_of_Collision','Hour_of_Collision','Special_Conditions_at_Site'], axis = 1)

imputer = Imputer(missing_values = 'NaN', strategy = 'most_frequent', axis = 1)
imputer = imputer.fit(x)
x = imputer.transform(x)
x[:5]

imputer = Imputer(missing_values = 'NaN', strategy = 'most_frequent', axis = 1)
imputer = imputer.fit(l)
l = imputer.transform(l)
l[:5]

#X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=.33)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=.20, stratify = y)


#clf = RandomForestClassifier(max_depth=6, n_estimators=10, max_features=1)
#clf = AdaBoostClassifier(learning_rate = 1)
#clf = SVC(kernel="linear", C=0.025)
#clf = KNeighborsClassifier(3)
#clf = GradientBoostingClassifier(learning_rate=1, n_estimators=10, max_depth=9, min_samples_split=1200, min_samples_leaf=60, subsample=0.85, random_state=10, max_features=10, warm_start=True)
clf = GradientBoostingClassifier(min_samples_split= 20, learning_rate= 0.15, max_depth= 4, n_estimators= 50)
clf.fit(x,y)

score = clf.score(X_test, y_test)
print(len(X_test))

print(score)
result = []
result = clf.predict(l)

l = []
for i in range(1,355):
    l.append(i)
df = pd.DataFrame(list(zip(l,result)), columns=["S.No.","Collision_Severity"])
df.to_csv('result2.csv', index=False)

