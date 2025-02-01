import cv2 
import os

img = cv2.imread(os.path.join('.','opencv/data/flock_of_birds.jpg'))
# it is best to take a binary image for contour detection

# convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('thresh', thresh)

# find contours - contours are the boundaries of the isolated regions in an image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if cv2.contourArea(cnt) > 200: # why - to avoid small contours
        cv2.drawContours(img, [cnt], -1, (0,255,0), 3)
        # image, contours, contour_index, color, thickness
        # contour_index = -1 means all contours

        # bounding rectangle - used to draw a rectangle around the contour
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imshow('contours', img)
cv2.waitKey(0)