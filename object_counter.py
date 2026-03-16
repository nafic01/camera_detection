import cv2
import numpy as np

cam = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION) # I am using a macbook, so I need to specify the backend. If you are using Windows or Linux, you can simply use cv2.VideoCapture(0)

if not cam.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cam.read()
    if not ret:
        break # safety check to ensure we have a valid frame

    frame = cv2.resize(frame, (1920, 1080))

    cv2.imshow("Camera", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

