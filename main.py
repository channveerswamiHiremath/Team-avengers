import cv2
import numpy as np
import os

# Load the known face images and their names
known_face_images = []
known_face_names = []

# Load the known face images
for filename in os.listdir():
    if filename.endswith('.jpg'):
        image = cv2.imread(os.path.join('known_faces', filename))
        known_face_images.append(image)
        known_face_names.append(filename.split('.')[0])

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load the face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Only process every other frame of video to save time
    if process_this_frame:
        # Convert the image from BGR color (which OpenCV uses) to RGB color
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the current frame of video
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        face_locations = []
        face_encodings = []
        face_names = []
        for (x, y, w, h) in faces:
            # Extract the face ROI
            roi = frame[y:y+h, x:x+w]

            # Convert the ROI to grayscale
            gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

            # Calculate the eigenvalues and eigenvectors of the ROI
            eigenvalues, eigenvectors = cv2.PCACompute(gray_roi, mean=None)

            # Calculate the face encoding
            face_encoding = np.concatenate((eigenvalues, eigenvectors))

            # Add the face location, encoding, and name to the lists
            face_locations.append((x, y, w, h))
            face_encodings.append(face_encoding)
            face_names.append("Unknown")

    process_this_frame = not process_this_frame

    # Display the results
    for (x, y, w, h), name in zip(face_locations, face_names):
        # Draw a box around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (x, y+h-35), (x+w, y+h), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (x + 6, y+h-6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
