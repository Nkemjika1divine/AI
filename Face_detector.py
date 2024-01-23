#!/usr/bin/python3
import cv2
from random import randrange

# open the haarcascade_frontalface_default.xml file
frontface = cv2.CascadeClassifier("frontalface_default.xml")

"""
# import the image usin cv2.imread
image = cv2.imread("avengers.jpg")

# change it to grayscale using cvtColor
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# This ensures that the coordinates of the faces in the images are recognized and stored no matter the size
face_cordinates = frontface.detectMultiScale(gray_image)
print(face_cordinates)

# print the rectangle on the face
# first argument is the image, second argument is two tuples of the face's coordinates, 3rd argument is the tuple of color combination, 4th argument is the tickness of the line
# but first, store the lists into a tuple that can be passed to the rectangle method
# randrange is to give it multiple shades of a color
for (x, y, w, h) in face_cordinates:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, randrange(255), 0), 2)


# to show the picture
cv2.imshow("This is our Photo", image)
"""

# or rather import a video
# however, if you want to make use of your webcam, you say cv2.VideoCapture(0)
vid = cv2.VideoCapture("cillian.mp4")

# make a while loop that runs throughout the duration of the video
while True:
    # read the content of the video
    success, frame = vid.read()

    # change it to grayscale using cvtColor
    gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_cordinates = frontface.detectMultiScale(gray_video)

    cv2.imshow("This is our Photo", gray_video)
    
    cv2.waitKey(1)

# this is used to make the program wait for execution. it keeps the image open for viewing
# cv2.waitKey()



print("Code completed")
