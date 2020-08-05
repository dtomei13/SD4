import face_recognition
import cv2
import numpy as np


def drawRectangle(image):
    # gets the location of my face
    faceLocation = face_recognition.face_locations(image)[0]
    # draws rectangle around the face for encoding
    cv2.rectangle(image, (faceLocation[3], faceLocation[0]), (faceLocation[1], faceLocation[2]), (255, 0, 0), 2)


# Loads the first picture I took for picture encoding
imageDylan = face_recognition.load_image_file('KnownFaces/Dylan/DylanEncoding.jpg')
# converts from BGR to RGB color fields
imageDylan = cv2.cvtColor(imageDylan, cv2.COLOR_BGR2RGB)
# Loads a test image to see if it learned my face
imageTest = face_recognition.load_image_file('KnownFaces/Dylan/Dylan4.jpg')
# imageTest = face_recognition.load_image_file('Unknown Faces/Woman.jpg')
imageTest = cv2.cvtColor(imageTest, cv2.COLOR_BGR2RGB)
# test bool
isLocked = True
print(f'isLocked is {isLocked}')

drawRectangle(imageDylan)
# encodes the image
encodeDylan = face_recognition.face_encodings(imageDylan)[0]
drawRectangle(imageTest)
# encodes the image
encodeTest = face_recognition.face_encodings(imageTest)[0]
# compares the known faces
results = face_recognition.compare_faces([encodeDylan], encodeTest)
faceDistance = face_recognition.face_distance([encodeDylan], encodeTest)
# prints the results on the image itself
cv2.putText(imageTest, f'{results} {round(faceDistance[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0),
            2)
if faceDistance < 0.5:
    isLocked = False
    print(f'isLocked is {isLocked}')
elif faceDistance > 0.5:
    print(f'isLocked is {isLocked}')


def showImage():
    # shows the images
    cv2.imshow('Dylan Image', imageDylan)
    cv2.imshow('Dylan Image Test', imageTest)


# waits until I hit the q button to end the program
if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
