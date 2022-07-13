import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split


def model (n, img_size):
    kn = KNeighborsClassifier(n_neighbors=n)
    fruits = np.load('my_data.npy')
    labels = np.load('my_label.npy')
    # fruits_2d = fruits.reshape(-1, img_size*img_size)
    
    kn.fit(fruits, labels)
    return kn
def test_model(n):
    kn = KNeighborsClassifier(n_neighbors=n)
    fruits = np.load('my_data.npy')
    labels = np.load('my_label.npy')
    avg_list = list()
    for i in range(100):
        train_data, test_data, train_label, test_label = train_test_split(fruits, labels, test_size=0.25)
        kn.fit(train_data, train_label)
        avg_list.append(kn.score(test_data, test_label))

    print("모델의 성능은 ", round(np.mean(avg_list)*100, 2), "점 입니다.")
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