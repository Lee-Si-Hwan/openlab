import cv2
import prepareingData
from npy_save_hsv import make_histogram
import model
import numpy as np
import os

img_size = 50
color_lb = 0
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = capture.read()
    if not ret:
        print("Can't read camera")
        break
        
    cv2.imshow("VideoFrame", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        print("q")
        break

    if key == ord('c'):
        print("C")
        img_captured = cv2.imwrite('img_captured.png', frame)
        print("사진이 저장되었습니다.")
        print("초콜릿을 분류 기계에 올려두고 분류 버튼 B를 누르세요")
    
    if key == ord('b'):
        print("B")
        kn = model.model(7, img_size)
        print(kn.labels_)

        img = cv2.imread("img_captured.png")
        img  = cv2.resize(img, dsize=(img_size, img_size))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, _, _ = cv2.split(hsv)
        data = np.array([h])
        data_2d = data.reshape(-1, img_size*img_size)
        print(kn.predict(data_2d))
        color_lb = int(kn.predict(data_2d))
        print("올바르게 분류되었나요?(y/n)")
        
    if key == ord('s'):
        print("S")
        data = prepareingData.get_histogram('./img_captured.png')
        print("Done")
    
    if key == ord('y'):
        print("올바르게 분류하였군요!")
        path_source = './img_captured.png'
        
        if color_lb == 0:
            path_dest = './red/'
            clb = len(os.listdir("./red"))+1
        else:
            path_dest = './blue/'
            clb = len(os.listdir("./blue"))+1
        os.replace(path_source , path_dest + f"{clb}.png")
        make_histogram()
        print("학습에 반영되었습니다!")
        pass 

    if key == ord('n'):
        print("올바르지 않군요!")
        path_source = './img_captured.png'
        
        if color_lb == 0:
            path_dest = './blue/'
            clb = len(os.listdir("./blue"))+1
        else:
            path_dest = './red/'
            clb = len(os.listdir("./red"))+1
        os.replace(path_source , path_dest + f"{clb}.png")
        make_histogram()
        print("학습에 반영되었습니다!")
        pass
        
capture.release()
cv2.destroyAllWindows()