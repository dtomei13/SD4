import cv2
import numpy as np

image = cv2.imread("Resources/Dylan.jpg")

imageHor = np.hstack((image, image))
imageVer = np.vstack((image, image))

cv2.imshow("Horizontal", imageHor)
cv2.imshow("Vertical", imageVer)

cv2.waitKey(0)
