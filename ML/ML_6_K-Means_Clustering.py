
#Unsupervised Learning
#Find clusters (k-clusters)
#When a new point - assign a cluster to it

#Whichever random centroid is closest to the 
#point is the cluster that the point belongs to

import sklearn.cluster
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits

digits = load_digits()
data = scale(digits)

model = sklearn.cluster.KMeans(n_clusters=10, init='random',n_init=10)
model.fit(data)

model.predict([...])


