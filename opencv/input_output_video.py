
import cv2
import os

video_path = os.path.join('.','opencv/data/ball_oscillation.mp4')

# read the video file
cap = cv2.VideoCapture(video_path)

# check if the video file is opened
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# visualize the video
ret = True
# will loop until the video ends
while ret:
    # read the frame
    ret, frame = cap.read()

    # check if the frame is read
    if not ret:
        print("Error: Could not read frame.")
        break

    # display the frame
    cv2.imshow("Video", frame)

    # check if the user wants to exit
    # press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video memory
cap.release()
# close the window
cv2.destroyAllWindows()