import cv2
image=cv2.imread("Ninetales.png")
garyimg=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invertimg=255-garyimg
blurimg=cv2.GaussianBlur(invertimg,(21,21),0)
intert_blurimg=255-blurimg
pencilsketch=cv2.divide(garyimg,intert_blurimg,scale=255)
cv2.imshow("Original",image)
cv2.imshow("Gary",pencilsketch)
cv2.waitKey(0)