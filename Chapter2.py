import cv2
import numpy as np

image = cv2.imread("Resources/Dylan.jpg")
kernel = np.ones((5, 5), np.uint8)

imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # converts the imported image to gray scale
imageBlur = cv2.GaussianBlur(imageGray, (11, 11), 0)  # must be odd numbers
imageCanny = cv2.Canny(image, 100, 200)
imageDialation = cv2.dilate(imageCanny, kernel, iterations=1)  # changes thickness of white lines from the canny
imageEroded = cv2.erode(imageDialation, kernel, iterations=1)

# cv2.imshow("Gray Image", imageGray)
# cv2.imshow("Blur Image", imageBlur)
cv2.imshow("Canny Image", imageCanny)
cv2.imshow("Dilation Image", imageDialation)
cv2.imshow("Eroded Image", imageEroded)
cv2.waitKey(0)  # waits forever....
