import cv2

# this is the classifier for cars and humans
human_body = cv2.CascadeClassifier("fullbody.xml")
car_body = cv2.CascadeClassifier("cars.xml")

# read the image file
image = cv2.imread("girl.jpg")

# change the image to B&W
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# get coordinates for the body and the cars
body = human_body.detectMultiScale(gray_image)
car = car_body.detectMultiScale(gray_image)

# print the body and cars coordinates
print(body)
print(car)

# get in here if there's a coordinate retrieved for either car or body
if body or car:

    # set coordinates for body
    x, y, w, h = body
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # show image for the picture alongside the coordinates
    cv2.imshow("The Image", gray_image)
    cv2.waitKey()
else:
    print("Found no coordinates")



print("Code completed")