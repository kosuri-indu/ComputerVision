import cv2
import os

img = cv2.imread(os.path.join('.','opencv/data/bird.jpg'))

# resize operation

print('Original Dimensions : ', img.shape)
cv2.imshow('Image', img)
resized_img = cv2.resize(img, (640, 480))
print('Resized Dimensions : ', resized_img.shape) # output - (480, 640, 3), first width, height, and then number of channels
cv2.imshow('Resized Image', resized_img) 

# crop operation

cropped_img = img[:, 420:840]
cv2.imshow('Cropped Image', cropped_img)

cv2.waitKey(0)