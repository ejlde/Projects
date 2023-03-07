# Is mark going out in nature
# Multiple event where he did and didnt
# Cases when he did and didnt

# Dataset of events

from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


data = load_breast_cancer()
x=data.data
y = data.target

# Splitting into training and testing data 
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
# random_state = specific data (NOT RANDOM)

clf = SVC(kernel='linear',C=3) #polynomial #rbf
clf.fit(x_train,y_train)

clf2 = KNeighborsClassifier(n_neighbors=3)
clf2.fit(x_train,y_train)

clf3 = DecisionTreeClassifier()
clf3.fit(x_train,y_train)

clf4 = RandomForestClassifier()
clf4.fit(x_train,y_train)

print(f'SVC: {clf.score(x_test,y_test)}') # Support vec has higher accuracy %
print(f'KNN: {clf2.score(x_test,y_test)}')
print(f'DTC: {clf3.score(x_test,y_test)}')
print(f'RFC: {clf4.score(x_test,y_test)}')

