import cv2
import os

img = cv2.imread(os.path.join('.','opencv/data/bird.jpg'))
cv2.imshow('Original', img)

# edge detection - detect edges in the image
edges_img = cv2.Canny(img, 50, 200) # 100 and 200 are the threshold values,there is a technique to find these values, but trial and error is the most common way
cv2.imshow('Edges', edges_img)

# types of edge detection
# Sobel, Scharr, Laplacian, Canny
# Canny edge detection is the most popular

# dilating the image - making the edges thicker
dilated_img = cv2.dilate(edges_img, (3, 3), iterations=1) # kernel size ,iterations is the number of times the dilation is applied
cv2.imshow('Dilated Edges', dilated_img)

# eroding the image - making the edges thinner
eroded_img = cv2.erode(dilated_img, (3, 3), iterations=1)
cv2.imshow('Eroded Edges', eroded_img)

cv2.waitKey(0)

