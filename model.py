import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.linear_model import SGDClassifier


def model (n, img_size):
    kn = KNeighborsClassifier(n_neighbors=n)
    fruits = np.load('my_data.npy')
    labels = np.load('my_label.npy')
    # fruits_2d = fruits.reshape(-1, img_size*img_size)
    
    kn.fit(fruits, labels)
    print(kn.score(fruits, labels))
    return kn

# def model (n, img_size):
#     # kn = KNeighborsClassifier(n_neighbors=n)
#     sc = SGDClassifier(loss='log', max_iter=5, random_state=42)
#     fruits = np.load('my_data.npy')
#     labels = np.load('my_label.npy')
    
#     fruits_2d = fruits.reshape(-1, img_size*img_size)
#     print(fruits_2d.shape)
    
#     # kn.fit(fruits_2d, labels)
#     km.fit(fruits_2d)
#     print(km.labels_)
#     return km
"""
이거 지금 다른 모델로 잠시 대체해봄
"""