#!/usr/bin/python3
import cv2

# open the haarcascade_frontalface_default.xml file
frontface = cv2.CascadeClassifier("frontalface_default.xml")

# import the image usin cv2.imread
image = cv2.imread("CE.jpg")

# change it to grayscale using cvtColor
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# This ensures that the coordinates of the faces in the images are recognized and stored no matter the size
face_cordinates = frontface.detectMultiScale(gray_image)
print(face_cordinates)

# print the rectangle on the face
# first argument is the image, second argument is two tuples of the face's coordinates, 3rd argument is the tuple of color combination, 4th argument is the tickness of the line
cv2.rectangle(image, (80, 181), (415, 415), (0, 0, 255), 2)


# to show the picture
cv2.imshow("This is our Photo", image)

# this is used to make the program wait for execution. it keeps the image open for viewing
cv2.waitKey()



print("Code completed")
