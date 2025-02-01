import cv2
import os

img = cv2.imread(os.path.join('.','opencv/data/bird.jpg'))
cv2.imshow('Original', img)
cv2.waitKey(0)

# thresholding - used to create binary images
# binary image - image with only two colors, black and white

# opencv provides four types of thresholding techniques
# 1. Binary - cv2.THRESH_BINARY
# 2. Binary Inverted - cv2.THRESH_BINARY_INV
# 3. Truncate - cv2.THRESH_TRUNC
# 4. To Zero - cv2.THRESH_TOZERO

# 1. Binary
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
# 127 - threshold value, 255 - max value, if pixel value > threshold value, it is assigned max value, else 0
cv2.imshow('Binary', binary_img)
cv2.waitKey(0)

# note - thresholding is used for creating segmentation masks

# 2. Binary Inverted
ret, binary_inv_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Binary Inverted', binary_inv_img)
cv2.waitKey(0)

# 3. Truncate - used to truncate the pixel values above the threshold value
ret, truncate_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow('Truncate', truncate_img)
cv2.waitKey(0)

# Adaptive thresholding - used when the threshold value is not fixed
# the threshold value is calculated for smaller regions of the image
adaptive_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# we can also have cv2.ADAPTIVE_THRESH_GAUSSIAN_C
# 255 - max value, cv2.ADAPTIVE_THRESH_MEAN_C - mean of the neighborhood area, 11 - block size, 2 - constant subtracted from the mean
cv2.imshow('Adaptive Thresholding', adaptive_img)
cv2.waitKey(0)
# works well for images with varying illumination



# when to use which thresholding technique
# 1. Binary - used to create a binary image
# 2. Binary Inverted - used to create a binary image with inverted colors
# 3. Truncate - used to truncate the pixel values above the threshold value
# 4. To Zero - used to convert the pixel values below the threshold
# 5. To Zero Inverted - used to convert the pixel values above the threshold