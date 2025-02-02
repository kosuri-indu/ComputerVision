import cv2
import utils
from PIL import Image

# Separation of Color Components
# HSV separates color information into three distinct components: Hue, Saturation, and Value. Unlike RGB, this separation makes it easier to detect and analyze colors. Specifically:
# - Hue represents the actual color type
# - Saturation indicates color intensity
# - Value shows brightness

# Define color ranges in BGR format
blue = [255, 0, 0]
orange = [0, 255, 255]

# Webcam capture
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get the lower and upper HSV limits for the color white
    lower_limit, upper_limit = utils.get_limits(color=orange)
    
    # Create a mask that isolates the pixels within the specified HSV range
    mask = cv2.inRange(hsv_img, lower_limit, upper_limit)

    # Convert the mask (a numpy array) to a PIL Image for further processing
    mask_ = Image.fromarray(mask)

    # Get the bounding box of the non-zero elements in the mask
    # Scans the image pixel by pixel to find the first and last non-zero pixels
    bbox = mask_.getbbox()
    print(bbox)

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        # Draw the bounding box on the original frame
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()