import cv2
import time
import os

# Load face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open webcam
cap = cv2.VideoCapture(0)

# Variables
last_face_time = time.time()
timeout = 15  # Seconds before locking

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to access webcam.")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        last_face_time = time.time()  # Reset timer if face detected
        # Optional: Uncomment to debug face detection
        # for (x, y, w, h) in faces:
        #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    else:
        if time.time() - last_face_time >= timeout:
            print("No face detected for 5 seconds, locking PC...")
            os.system("rundll32.exe user32.dll,LockWorkStation")  # Lock the PC using Windows command
            time.sleep(5)  # Wait before checking again
            last_face_time = time.time()

    # Optional: Uncomment to see webcam feed
    # cv2.imshow('Webcam - Face Detection', frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

    time.sleep(0.1)  # Small delay to reduce CPU usage

# Cleanup
cap.release()
cv2.destroyAllWindows()
