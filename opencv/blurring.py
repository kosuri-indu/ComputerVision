import cv2
import os

img = cv2.imread(os.path.join('.','opencv/data/bird.jpg'))
cv2.imshow('Original', img)

# blurring - we calculate the average of the pixel values in the neighborhood of a pixel and replace the pixel value with the average value
# It is a technique used to reduce the noise in an image
# noise - random variations of brightness or color information in images, those dots that are not part of the image

# opencv provides four types of blurring techniques
# 1. Averaging - blur()
# 2. Gaussian - GaussianBlur()
# 3. Median - medianBlur()
# 4. Bilateral - bilateralFilter()

# 1. Averaging - most commonly used
blur_img = cv2.blur(img, (5,5)) # (5,5) is the kernel size, (k_w, k_h) to computer averages
cv2.imshow('Averaging', blur_img)

# 2. Gaussian - used to remove high frequency noise from the image
gaussian_img = cv2.GaussianBlur(img, (5,5), 0) 
# 0 - standard deviation in x direction (same is taken for y direction, if not specifically defined), 0 means it is calculated automatically based on the kernel size
cv2.imshow('Gaussian', gaussian_img)

# 3. Median - used to remove salt and pepper noise - noise that is randomly distributed in an image
median_img = cv2.medianBlur(img, 5) # 5 is the kernel size
cv2.imshow('Median', median_img)

# when to use which blurring technique
# 1. Averaging & Gaussian - when the noise is random and uniformly distributed
# 2. Median - when the noise is random and not uniformly distributed
# 3. Bilateral - when we want to preserve the edges in the image

cv2.waitKey(0)
