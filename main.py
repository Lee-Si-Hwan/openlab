import cv2
import prepareingData

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
        print("Done")
        
    if key == ord('q'):
        print("q")
        break
    
    if key == ord('s'):
        print("S")
        data = prepareingData.get_histogram('./img_captured.png')
        print("Done")
        
capture.release()
cv2.destroyAllWindows()