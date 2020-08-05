import cv2

# Read images from computer and webcam

cap = cv2.VideoCapture(0)   # Takes image from default webcam

cap.set(3, 1920)  # sets the width
cap.set(4, 1080)  # sets the height
cap.set(10, 100)  # sets the brightness

while True:  # while loop to render the video
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
