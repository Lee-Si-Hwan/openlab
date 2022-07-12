import cv2, numpy as np
from sklearn.cluster import KMeans

fruits = np.load("multi_image_data.npy")

fruits_2d = fruits.reshape(-1, 100*100)

km = KMeans(n_clusters=3, random_state=42)
km.fit(fruits_2d)

print(km.labels_)

