import cv2
import os

img = cv2.imread(os.path.join('.','opencv/data/bird.jpg'))

cv2.imshow('Image', img)

# note - OpenCV reads images in BGR format, not RGB
# what we are doing is just changing how this information is organized

# convert to RGB
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB Image', rgb_img)

# convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', gray_img)

# convert to HSV - Hue, Saturation, Value
# used to detect colors in an image
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image', hsv_img)

cv2.waitKey(0)


