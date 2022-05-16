import cv2

img = cv2.imread("butterfly.jpg")

cv2.imshow("output",img)

greyImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("greyImage",greyImg)

cv2.waitKey(0)