import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_alt.xml")

cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imageGray, 1.1, 4)

    for(x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)

    cv2.imshow("Video", image)
    cv2.imshow("Gray", imageGray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
