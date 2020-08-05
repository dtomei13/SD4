import cv2

import numpy as np

image = cv2.imread("Resources/Dylan.jpg")

width, height = 250, 350
points1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
points2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(points1, points2)
imageOutPut = cv2.warpPerspective(image, matrix, (width, height))


cv2.imshow("Image", image)
cv2.imshow("Image Output", imageOutPut)

cv2.waitKey(0)
