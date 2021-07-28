import cv2

img = cv2.imread('kirbyog.png')

low = (150, 50, 50)
high = (170, 255, 255)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(img_hsv, low, high)
f_img = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('blirb', f_img)
cv2.waitKey(0)