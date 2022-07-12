from ast import Pass
import cv2
import prepareingData
import sys

def mouse_click(event, x, y, flags, param):
    global img
    
    if event == cv2.EVENT_FLAG_LBUTTON:    
        cv2.circle(img, (x, y), 5, (0, 0, 255), 2)
        cv2.imshow("blank", img)
    elif event == cv2.EVENT_FLAG_RBUTTON:   
        img = np.full((800, 800, 3), 255, dtype=np.uint8) 
        cv2.imshow("blank", img)

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
    if key == ord('c'):
        print("C")
        img_captured = cv2.imwrite('img_captured.png', frame)
        print("올바르게 분류하였나요?(y/n)")
        
    if key == ord('q'):
        print("q")
        break
    
    if key == ord('s'):
        print("S")
        data = prepareingData.get_histogram('./img_captured.png')
        print("Done")
    
    if key == ord('y'):
        print("올바르게 분류하였군요!")
        print("학습에 반영되었습니다!")
        pass 

    if key == ord('n'):
        print("올바르지 않군요!")
        print("메뉴얼을 보고 알맞은 색 버튼을 눌러주세요!")
        pass
        
capture.release()
cv2.destroyAllWindows()