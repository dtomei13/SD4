import cv2
import numpy as np


faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_alt.xml")
image = cv2.imread('Resources/face.jpg')
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imageGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("Result", image)
cv2.waitKey(0)
