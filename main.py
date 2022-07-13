import cv2
import prepareingData
from npy_save_hsv import make_histogram
import model
import numpy as np
import os
import serial
import time

arduino = serial.Serial('com3',9600)

img_size = 100
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
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print("사진이 저장되었습니다.")
        print("초콜릿을 분류 기계에 올려두고 분류 버튼 B를 누르세요")
        
    
    if key == ord('b'):
        print("B")
        kn = model.model(3, img_size)

        img = cv2.imread("img_captured.png")
        img  = cv2.resize(img, dsize=(img_size, img_size))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hsv], [0], None, [180], [0, 180])
        hist = np.ravel(hist, order='C')#1차원으로 축소
        hist = hist[1:] #첫번째 값은 h가 0이므로 제거
        hist = hist / sum(hist)
        data = np.array([hist])
        print(kn.predict(data))
        color_lb = int(kn.predict(data))
        if color_lb == 0:
            var = '-1'
            arduino.write(var.encode('utf-8'))
        else:
            var = '1'
            arduino.write(var.encode('utf-8'))
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print("올바르게 분류되었나요?(y/n)")
        
    
    if key == ord('y'):
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
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
        pass 

    if key == ord('n'):
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
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
    
    if key == ord('t'):
        print("학습에 반영되었습니다!")
        model.test_model(3)
        
capture.release()
cv2.destroyAllWindows()