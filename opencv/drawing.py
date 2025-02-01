import cv2
import os

img = cv2.imread(os.path.join('.','opencv/data/bird.jpg'))
cv2.imshow('Original', img)

# drawing on the image

# line
cv2.line(img, (0, 0), (200, 200), (0, 255, 0), 5) 
# image, start point, end point, color, thickness
cv2.imshow('Line', img)

# rectangle
cv2.rectangle(img, (200, 200), (400, 400), (0, 0, 255), 5)
# image, top left corner, bottom right corner, color, thickness
# fill the rectangle - cv2.rectangle(img, (200, 200), (400, 400), (0, 0, 255), cv2.FILLED or -1)
cv2.imshow('Rectangle', img)

# circle
cv2.circle(img, (300, 300), 100, (255, 0, 0), 5)
# image, center, radius, color, thickness
cv2.imshow('Circle', img)

# text
cv2.putText(img, 'Hello', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)
# image, text, position, font, font size, color, thickness
cv2.imshow('Text', img)

cv2.waitKey(0)

