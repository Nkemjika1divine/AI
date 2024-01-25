import cv2

human_body = cv2.CascadeClassifier("fullbody.xml")

image = cv2.imread("avengers.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("The Image", gray_image)
cv2.waitKey()