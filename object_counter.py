import cv2
import numpy as np

def run(selected_colour):
    # (1=Red, 2=Green, 3=Blue)
    
    print("Object counter with colour:", selected_colour)

    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        ret, frame = cam.read()
        if not ret:
            break  # safety check

        frame = cv2.resize(frame, (1920, 1080))

        if selected_colour == 1: # Red
            # convert frame to HSV and create mask for red
            pass
        elif selected_colour == 2: # Green
            # convert frame to HSV and create mask for green
            pass
        elif selected_colour == 3: # Blue
            # convert frame to HSV and create mask for blue
            pass

        cv2.imshow("Camera", frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break  # exit loop safely

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # If run directly, default to Red (1)
    run(1)