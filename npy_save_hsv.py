from PIL import Image
import os, glob, cv2, numpy as np
from sklearn.model_selection import train_test_split

#groups_folder_path = 'C:/Users/user/Desktop/colorgroup'
categories = ["red","blue","brown","orange","green","yellow"]
nb_classes = len(categories) #카테고리갯수: 6개

image_w = 600 #이미지의 크기를 모두 통일해준다
image_h = 600


X = []
y = []
H = []
for idx, cat in enumerate(categories):
    
    #one-hot 돌리기.

    image_dir = "C:/Users/csi2/Documents/GitHub/openlab/img_captured.png"
    src = cv2.imread(image_dir, cv2.IMREAD_COLOR)
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    print(type(h), h[:100])
        
        

    X.append(data) #리스트에 추가 
    y.append(label)
    H.append(h)
    break

print(H)
print(X)
X = np.array(X)
y = np.array(y)
H = np.array(H)
print(H)
print(X)
#1 0 0 0 이면 느타리버섯
#0 1 0 0 이면 새송이버섯

#X_train, X_test, y_train, y_test = train_test_split(X, y) #데이터를 훈련셋과 시험셋으로 나눠주는 함수이용
#xy = (X_train, X_test, y_train, y_test)
np.save("multi_image_data_h.npy", H) #그렇게 X를 multi_image_data.npy로 저장

print("ok", len(y))
#abc=np.load('multi_image_data.npy', allow_pickle=True)
print(H.shape)
#print(y)
