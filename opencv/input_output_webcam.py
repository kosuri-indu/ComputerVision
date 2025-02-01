import cv2

# read the webcam
# 0 - default webcam
# 1 - external webcam
# 2 - another external webcam etc
cap = cv2.VideoCapture(0)

# check if the webcam is opened
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# visualize the webcam
while True:
    # read the frame
    ret, frame = cap.read()

    # check if the frame is read
    if not ret:
        print("Error: Could not read frame.")
        break

    # display the frame
    cv2.imshow("Webcam", frame)

    # check if the user wants to exit
    # press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the webcam memory
cap.release()
# close the window
cv2.destroyAllWindows()