#!/usr/bin/python3
import cv2

# open the haarcascade_frontalface_default.xml file
frontface = cv2.CascadeClassifier("frontalface_default.xml")

# import the image usin cv2.imread
image = cv2.imread("CE.jpg")

# to show the picture
cv2.imshow("This is our Photo", image)

# this is used to make the program wait for execution
cv2.waitKey()



print("Code completed")
