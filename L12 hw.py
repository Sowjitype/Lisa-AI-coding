import numpy as np
import cv2
import os
DEBUG = True

def print_debug(msg):
    if DEBUG:
        print(f"[DEBUG] {msg}")
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("[ERROR] Could not open camera (check if another app is using it)")
    exit(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
print_debug(f"Camera resolution: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}x{cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
cv2_data_path = cv2.data.haarcascades
face_cascade = cv2.CascadeClassifier(os.path.join(cv2_data_path, 'haarcascade_frontalface_default.xml'))
eye_cascade = cv2.CascadeClassifier(os.path.join(cv2_data_path, 'haarcascade_eye.xml'))
if face_cascade.empty():
    print("[ERROR] Failed to load face cascade (missing file in OpenCV data)")
    cap.release()
    exit(1)
if eye_cascade.empty():
    print("[ERROR] Failed to load eye cascade")
    cap.release()
    exit(1)
print_debug("Face/Eye cascades loaded successfully")
USE_EAR_DETECTION = False  # Set to True only if you have the XML files
left_ear_cascade = None
right_ear_cascade = None

if USE_EAR_DETECTION:
    # Download ear cascades from: https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_mcs_leftear.xml
    ear_cascade_path = "./cascade_files"  # Update this path!
    left_ear_path = os.path.join(ear_cascade_path, 'haarcascade_mcs_leftear.xml')
    right_ear_path = os.path.join(ear_cascade_path, 'haarcascade_mcs_rightear.xml')
    if not os.path.exists(left_ear_path):
        print(f"[ERROR] Left ear cascade not found at: {left_ear_path}")
        USE_EAR_DETECTION = False
    if not os.path.exists(right_ear_path):
        print(f"[ERROR] Right ear cascade not found at: {right_ear_path}")
        USE_EAR_DETECTION = False
    if USE_EAR_DETECTION:
        left_ear_cascade = cv2.CascadeClassifier(left_ear_path)
        right_ear_cascade = cv2.CascadeClassifier(right_ear_path)
        if left_ear_cascade.empty() or right_ear_cascade.empty():
            print("[ERROR] Corrupted ear cascade files")
            USE_EAR_DETECTION = False
        else:
            print_debug("Ear cascades loaded successfully")
while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Failed to read frame (camera disconnected?)")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print_debug(f"Frame shape: {frame.shape} | Grayscale shape: {gray.shape}")
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,  # More precise than 1.3 (better for small faces)
        minNeighbors=5,
        minSize=(30, 30)  # Ignore tiny false positives
    )
    print_debug(f"Detected {len(faces)} faces")
    for (x_face, y_face, w_face, h_face) in faces:
        cv2.rectangle(frame, (x_face, y_face), (x_face + w_face, y_face + h_face), (255, 0, 0), 2)
        roi_gray = gray[y_face:y_face + h_face, x_face:x_face + w_face]  # Fixed: h_face (not w_face)
        roi_color = frame[y_face:y_face + h_face, x_face:x_face + w_face]
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5)
        print_debug(f"Detected {len(eyes)} eyes in face")

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (100, 205, 0), 2)
    if USE_EAR_DETECTION:
        left_ear = left_ear_cascade.detectMultiScale(gray, scaleFactor=1.7, minNeighbors=3)
        right_ear = right_ear_cascade.detectMultiScale(gray, scaleFactor=1.7, minNeighbors=3)
        print_debug(f"Detected {len(left_ear)} left ears | {len(right_ear)} right ears")
        for (x_le, y_le, w_le, h_le) in left_ear:
            cv2.rectangle(frame, (x_le, y_le), (x_le + w_le, y_le + h_le), (0, 255, 0), 2)
        for (x_re, y_re, w_re, h_re) in right_ear:
            cv2.rectangle(frame, (x_re, y_re), (x_re + w_re, y_re + h_re), (0, 255, 255), 2)
    cv2.imshow('Face/Eye/Ear Detection (Press Q to Quit)', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print_debug("Q pressed - exiting...")
        break
cap.release()
cv2.destroyAllWindows()
print_debug("Cleanup complete - program exited safely")