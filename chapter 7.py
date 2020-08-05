import cv2
import numpy as np


# empty method as a passer
def empty(a):
    pass


# Method the video dude made
def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


# all of the track bar variables that can be adjusted
path = 'Resources/car.jpg'
cv2.namedWindow("Track Bars")
cv2.resizeWindow("Track Bars", 640, 240)
cv2.createTrackbar("Hue Min", "Track Bars", 8, 179, empty)
cv2.createTrackbar("Hue Max", "Track Bars", 20, 179, empty)
cv2.createTrackbar("Sat Min", "Track Bars", 56, 255, empty)
cv2.createTrackbar("Sat Max", "Track Bars", 255, 255, empty)
cv2.createTrackbar("Val Min", "Track Bars", 157, 255, empty)
cv2.createTrackbar("Val Max", "Track Bars", 255, 255, empty)

# loop to update the track bar values in real time
while True:
    image = cv2.imread(path)
    imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "Track Bars")
    h_max = cv2.getTrackbarPos("Hue Max", "Track Bars")
    s_min = cv2.getTrackbarPos("Sat Min", "Track Bars")
    s_max = cv2.getTrackbarPos("Sat Max", "Track Bars")
    v_min = cv2.getTrackbarPos("Val Min", "Track Bars")
    v_max = cv2.getTrackbarPos("Val Max", "Track Bars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imageHSV, lower, upper)
    imageResult = cv2.bitwise_and(image, image, mask=mask)

    imageStack = stackImages(0.6, ([image, imageHSV], [mask, imageResult]))
    cv2.imshow("Stacked Images", imageStack)
    cv2.waitKey(1)
