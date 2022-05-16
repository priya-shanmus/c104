import cv2

img = cv2.imread("poster.jpg")

rocket = img[100:300,400:500]

img[50:250,500:600] = rocket

text_in_image = "Hi this is c104 with gayathri"

cv2.putText(img,text_in_image,(20,120),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,0,255))



cv2.imshow("greeting",img)

cv2.waitKey(0)