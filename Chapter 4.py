import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)
#print(image.shape)
#image[:]= 255, 0, 0
cv2.line(image, (0, 0), (image.shape[1], image.shape[0]), (0, 255, 0), 3)
cv2.rectangle(image, (0,0), (250, 350), (0, 0, 255), cv2.FILLED)
cv2.circle(image, (400, 50), 30, (255, 255, 0), 5)
cv2.putText(image, "Butt Face", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (150, 192, 0), 1)

cv2.imshow("Image", image)

cv2.waitKey(0)