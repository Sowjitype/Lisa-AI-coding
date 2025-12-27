import cv2
import cv2.data

# load the pre trained Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# start video capture from default cam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: could not open camera")
    exit()

while True:
    #capture frame by frame
    ret, frame = cap.read()

    # if frame is read correctly, ret will be true
    if not ret:
        print("Error: failed to capture image")
        break

    # convert frame to grayscale (face detection works better on grayscale)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detec face in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # draw rectangle around face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # blue rectangle with thickness 2

        # display resulting frame
    cv2.imshow("Face Detection - press q for quit", frame)

    # break the loops when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# release the capture and close any open windows
cap.release()
cv2.destroyAllWindows()