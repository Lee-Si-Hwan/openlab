import cv2
import prepareingData
from npy_save_hsv import make_histogram
import model
import numpy as np
import os
import serial
import time

arduino = serial.Serial('com4',9600)

img_size = 100
color_lb = 0
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

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
        img_captured = cv2.imwrite('img_captured.png', frame)
        print()
        print()
        print()
        print()
        print()
        print()
        print("===================================================")
        print()
        print("사진이 저장되었습니다.")
        print("초콜릿을 분류 기계에 올려두고 분류 버튼 B를 누르세요")
        print()
        print("===================================================")
        print()
        
    
    if key == ord('b'):
        kn = model.model(4, img_size)

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
            print("빨간색입니다.")
            print()
            var = '1'
            arduino.write(var.encode('utf-8'))
        elif color_lb == 1:
            print("파란색입니다.")
            print()
            var = '2'
            arduino.write(var.encode('utf-8'))
        else:
            print("초록색입니다.")
            print()
            var = '3'
            arduino.write(var.encode('utf-8'))
        print()
        print("올바르게 분류되었나요?(y/n)")
        print("올바르게 분류했으면 Y를 누르고 아니면 알맞는 색의 버튼을 누르세요")
        print()
        print("===================================================")
        
    
    if key == ord('y'):
        print()
        print()
        print()
        print()
        print()
        print()
        print("===================================================")
        print()
        print("올바르게 분류하였군요!")
        path_source = './img_captured.png'
        
        if color_lb == 0:
            path_dest = './red/'
            clb = len(os.listdir("./red"))+1
        elif color_lb == 1:
            path_dest = './blue/'
            clb = len(os.listdir("./blue"))+1
        else:
            path_dest = './green/'
            clb = len(os.listdir("./green"))+1
        os.replace(path_source , path_dest + f"{clb}.png")
        make_histogram()
        
    
    if key == ord('i'):
        path_source = './img_captured.png'
        path_dest = './red/'
        clb = len(os.listdir("./red"))+1
        os.replace(path_source , path_dest + f"{clb}.png")
        make_histogram()
        print("학습에 반영되었습니다!")
        print()
        print("===================================================")
        pass
    if key == ord('o'):
        path_source = './img_captured.png'
        path_dest = './blue/'
        clb = len(os.listdir("./blue"))+1
        os.replace(path_source , path_dest + f"{clb}.png")
        make_histogram()
        print("학습에 반영되었습니다!")
        print()
        print("===================================================")
        pass
    if key == ord('p'):
        path_source = './img_captured.png'
        path_dest = './green/'
        clb = len(os.listdir("./green"))+1
        os.replace(path_source , path_dest + f"{clb}.png")
        make_histogram()
        print("학습에 반영되었습니다!")
        print()
        print("===================================================")
        pass
    
    if key == ord('t'):
        print("\n\n\n\n")
        print("잠시만 기다려 주세요...")
        print("현재 모델의 정확도 점수를 계산하고 있습니다!")
        print()
        print("===================================================")
        model.test_model(4)
        
capture.release()
cv2.destroyAllWindows()