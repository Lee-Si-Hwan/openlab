# import numpy as np
# from sklearn.cluster import KMeans

# fruits = np.load('my_data.npy')
# fruits_2d = fruits.reshape(-1, 600*600)

# km = KMeans(n_clusters=6, random_state=42)
# km.fit(fruits_2d)
# print(fruits_2d)
# print(km.labels_)
# print(np.unique(km.labels_, return_counts=True))
#print(fruits)

import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def model (n):
    kn = KNeighborsClassifier(n_neighbors=n)
    fruits = np.load('my_data.npy')
    labels = np.load('my_label.npy')
    fruits_2d = fruits.reshape(-1, 50*50)
    print(fruits_2d.shape)
    
    kn.fit(fruits_2d, labels)
    return kn



'''
0.6009523809523809
0.5504761904761905
0.48904761904761906
0.4971428571428571
0.48619047619047623
0.4647619047619048
0.4828571428571429
0.469047619047619
0.4457142857142857


'''