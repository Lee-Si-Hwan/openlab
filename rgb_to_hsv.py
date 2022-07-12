import cv2

src = cv2.imread('C:/Users/user/Desktop/coloruse/1r (1).jpg', cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

print(h)
print(len(h))
print(h[300,300])


#cv2.imshow("h", h)
#cv2.imshow("s", s)
#cv2.imshow("v", v)
#cv2.waitKey()
#cv2.destroyAllWindows()
