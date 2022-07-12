from PIL import Image
import os, glob, cv2, numpy as np
from sklearn.model_selection import train_test_split

#groups_folder_path = 'C:/Users/user/Desktop/colorgroup'
categories = ["red","blue"]
nb_classes = len(categories) #카테고리갯수: 6개

image_w = 50 #이미지의 크기를 모두 통일해준다
image_h = 50

def make_dataset(data, label):
    np.save('my_data.npy', data) # numpy.ndarray 저장. @파일명, @값
    data2 = np.load('my_data.npy') # 데이터 로드. @파일명

    np.save('my_label.npy', label) # numpy.ndarray 저장. @파일명, @값
    data2 = np.load('my_label.npy')
    print("uploaded")

def make_histogram():
    data = list()
    label = np.array([])

    for idx, cat in enumerate(categories):
        for i in os.listdir(cat):
            img = cv2.imread(cat+"/"+i)
            img  = cv2.resize(img, dsize=(image_w, image_h))
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            h, _, _ = cv2.split(hsv)
            data.append(list(h))
            print(h.shape)
            label = np.append(label, idx)
        
    data = np.array(data)
    make_dataset(data , label)
# print(data.shape)
# print(label.shape)
# print(data[:3])
# print(label)

#1 0 0 0 이면 느타리버섯
#0 1 0 0 이면 새송이버섯

#X_train, X_test, y_train, y_test = train_test_split(X, y) #데이터를 훈련셋과 시험셋으로 나눠주는 함수이용
#xy = (X_train, X_test, y_train, y_test)

#print(y)
