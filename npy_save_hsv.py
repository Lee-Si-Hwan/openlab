from PIL import Image
import os, glob, cv2, numpy as np
from sklearn.model_selection import train_test_split

groups_folder_path = 'C:/Users/user/Desktop/colorgroup'
categories = ["red","blue","brown","orange","green","yellow"]
nb_classes = len(categories) #카테고리갯수: 6개

image_w = 600 #이미지의 크기를 모두 통일해준다
image_h = 600


X = []
y = []
H = []
for idx, cat in enumerate(categories):
    
    #one-hot 돌리기.
    label = [0 for i in range(nb_classes)] #one-hot으로 라벨을 붙혀줌
    label[idx] = 1

    image_dir = groups_folder_path + "/" + cat
    files = glob.glob(image_dir+"/*.jpg")
    print(cat, " 파일 길이 : ", len(files))
    for i, f in enumerate(files):
        img = Image.open(f)      #폴더를 열어주고 이미지를 읽음
        img = img.convert("RGB")   #RGB로 바꿈
        img = img.resize((image_w, image_h)) #이미지 크기를 모두 학습시키기 쉽게 600x600크기고
        data = np.asarray(img) #숫자로
        src = cv2.imread(f, cv2.IMREAD_COLOR)
        hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        print(type(h))
        print(type(data))
        #for i in range(600):
            #for j in range(600):
                #data[i,j,0]=h[i,j]
        #print(data)
        
        

        X.append(data) #리스트에 추가 
        y.append(label)
        H.append(h)

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
