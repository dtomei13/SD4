import cv2
import numpy as np

image = cv2.imread("Resources/Dylan.jpg")
print(image.shape)

imageResize = cv2.resize(image, (320, 175)) # width, height

imageCropped = image[0:200, 200:500]  # height, width

cv2.imshow("Image", image)
cv2.imshow("Image Resized", imageResize)
cv2.imshow("Image Cropped", imageCropped)
cv2.waitKey(0)
