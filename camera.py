import cv2

cam = cv2.VideoCapture(0)

low = (100, 10, 10)
high = (120, 255, 255)

while True:
    ret, img = cam.read()

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img_hsv, low, high)

    f_img = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('my face', f_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break