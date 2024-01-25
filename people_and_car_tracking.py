import cv2

human_body = cv2.CascadeClassifier("fullbody.xml")

image = cv2.imread("girl.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

body = human_body.detectMultiScale(gray_image)

print(body)

if body:

    x, y, w, h = body
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)


    cv2.imshow("The Image", gray_image)
    cv2.waitKey()
else:
    print("Found no coordinates")



print("Code completed")