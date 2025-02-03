import os
import cv2
import mediapipe as mp # A library for building multimodal applied ML pipelines
import argparse # This library allows you to pass command-line arguments to the script,

def process_img(img, face_detection):
    # As MediaPipe works with RGB images. We need to convert the BGR image to RGB.
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detect faces in the image
    results = face_detection.process(img_rgb)

    if results.detections is not None:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = img.shape

            x = int(bboxC.xmin * iw)
            y = int(bboxC.ymin * ih)
            w = int(bboxC.width * iw)
            h = int(bboxC.height * ih)

            # Blur the detected face
            img[y:y+h, x:x+w] = cv2.blur(img[y:y+h, x:x+w], (30, 30))
    return img

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("--mode", default="webcam", help="Mode: image, video, or webcam")
parser.add_argument("--filePath", default="face.jpg", help="Path to the image or video file")
args = parser.parse_args()

output_dir = "./output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize face detection
mp_face_detection = mp.solutions.face_detection

# model_selection: 0: within short range, 1: within long range
# min_detection_confidence: Minimum confidence value ([0.0, 1.0]) from the face detection model for the detection to be considered successful.
with mp_face_detection.FaceDetection(min_detection_confidence=0.5, model_selection=0) as face_detection:

    if args.mode in ["image"]:
        img = cv2.imread(args.filePath)
        if img is None:
            print(f"Error: Could not read image {args.filePath}")
            exit()

        img = process_img(img, face_detection)
        # Save the anonymized image
        cv2.imwrite(os.path.join(output_dir, "output.jpg"), img)
    
    elif args.mode in ["video"]:
        cap = cv2.VideoCapture(args.filePath)
        if not cap.isOpened():
            print(f"Error: Could not open video file {args.filePath}")
            exit()

        ret, frame = cap.read()
        if not ret:
            print(f"Error: Could not read frame from video {args.filePath}")
            exit()

        # syntax: cv2.VideoWriter(output_file, fourcc, fps, frame_size)
        # fourcc: 4-character code of codec used to compress the frames
        # fps: frames per second (frame rate)
        output_video = cv2.VideoWriter(os.path.join(output_dir, "output.mp4"), cv2.VideoWriter_fourcc(*'MP4V'), 25, (frame.shape[1], frame.shape[0]))

        while ret:
            frame = process_img(frame, face_detection)

            # Write the frame to the output video
            output_video.write(frame)
            ret, frame = cap.read()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        output_video.release()

    elif args.mode in ["webcam"]:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open webcam.")
            exit()

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame from webcam.")
                break

            frame = process_img(frame, face_detection)
            cv2.imshow("Webcam", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()