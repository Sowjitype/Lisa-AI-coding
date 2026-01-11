import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from math import hypot
import screen_brightness_control as sbc

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

mp_draw = mp.solutions.drawing_utils

# Pycaw for volume control
try:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    volume_range = volume.GetVolumeRange()
    min_vol = volume_range[0]
    max_vol = volume_range[1]

except Exception as e:
    print(f"Error initializing Pycaw: {e}")
    exit()

# Webcam setup
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

while True:
    success, img = cap.read()

    if not success:
        print("Failed to read frame from webcam.")
        break    

    img = cv2.flip(img, 1) # Flip the image for a mirror effect
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)    

    if results.multi_hand_landmarks and results.multi_handedness:
        for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
            hand_label = results.multi_handedness[i].classification[0].label # 'Left' or 'Right'           

            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)            

            # Extract the tip of the thumb and index finger
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]            

            h, w, _ = img.shape
            thumb_pos = (int(thumb_tip.x * w), int(thumb_tip.y * h))
            index_pos = (int(index_tip.x * w), int(index_tip.y * h))           

            # Draw circles at the tips
            cv2.circle(img, thumb_pos, 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, thumb_pos, 10, (255, 0, 0), cv2.FILLED)
            cv2.line(img, thumb_pos, index_pos, (0, 255, 0), 3)            

            # Calculate the distance between thumb and index finger
            distance = hypot(index_pos[0] - thumb_pos[0], index_pos[1] - thumb_pos[1])

            if hand_label == "Right": # Control volume with the right hand
                vol = np.interp(distance, [30, 300], [min_vol, max_vol])
                try:
                    volume.SetMasterVolumeLevel(vol, None)

                except Exception as e:
                    print(f"Error adjusting volume: {e}")            

                # Visual feedback for volume
                vol_bar = np.interp(distance, [30, 300], [400, 150])

                cv2.rectangle(img, (50, 150), (85,400), (255, 0, 0), 2)
                cv2.rectangle(img, (50, int(vol_bar)), (85, 400), (255, 0, 0), cv2.FILLED)
                cv2.putText(img, f'Volume: {int(np.interp(distance, [30, 300], [0, 100]))}%', (40, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

            elif hand_label == "Left": # Control brightness with the left hand
                brightness = np.interp(distance, [30, 300], [0, 100])

                try:
                    sbc.set_brightness(brightness)

                except Exception as e:
                    print(f"Error adjusting brightness: {e}")

                # Visual feedback for brightness
                brightness_bar = np.interp(distance, [30, 300], [400, 150])
                cv2.rectangle(img, (100, 150), (135, 400), (0, 255, 0), 2)

                cv2.rectangle(img, (100, int(brightness_bar)), (135, 400), (0, 255, 0), cv2.FILLED)

                cv2.putText(img, f'Brightness: {int(brightness)}%', (90, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    # Show the video feed with annotations
    cv2.imshow("Gesture Volume and Brightness Controller", img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()