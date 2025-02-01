# pip install opencv-python
import cv2
import os

image_path = os.path.join('.','opencv/data/bird.jpg')
# read the image
img = cv2.imread(image_path)

# write the image
cv2.imwrite("data/tree_copy.jpg", img)

# display the image - this will open a window with the image but it will close immediately
cv2.imshow("Image", img)

cv2.waitKey(0) 
# waits for any key to be pressed
# 0 - wait indefinitely
# 1000 - wait for 1 second etc.