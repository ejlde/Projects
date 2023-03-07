# Parallel Support Vector from Baseline
# Margin area = free space betwen lines and baseline
# Used to classify data
# Very good
# Kernels - add extra dimension to data to separate

# Soft Margin

from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = load_breast_cancer()
x=data.data
y = data.target

# Splitting into training and testing data 
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=23)
# random_state = specific data (NOT RANDOM)

clf = SVC(kernel='linear',C=3) #polynomial #rbf
clf.fit(x_train,y_train)
clf2 = KNeighborsClassifier(n_neighbors=3)
clf2.fit(x_train,y_train )

print(f'SVC: {clf.score(x_test,y_test)}') # Support vec has higher accuracy %
print(f'KNN: {clf2.score(x_test,y_test)}')

