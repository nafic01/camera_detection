import cv2
import numpy as np

def run(selected_colour):
    # (1=Red, 2=Green, 3=Blue)

    print("Object counter with colour:", selected_colour)

    cam = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
    kernel = np.ones((5, 5), np.uint8)

    if not cam.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        frame = cv2.resize(frame, (1920, 1080))
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        if selected_colour == 1:  # Red
            mask = cv2.inRange(hsv, (0,120,70), (10,255,255)) | cv2.inRange(hsv, (170,120,70), (180,255,255))
            print("Red mask created")

        elif selected_colour == 2:  # Green
            mask = cv2.inRange(hsv, (36,25,25), (70,255,255))
            print("Green mask created")

        elif selected_colour == 3:  # Blue
            mask = cv2.inRange(hsv, (94,80,2), (126,255,255))
            print("Blue mask created")

        result = cv2.bitwise_and(frame, frame, mask=mask)
        cleaned = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_CLOSE, kernel)
        cv2.imshow("Camera", frame)
        cv2.imshow("Mask", mask)
        cv2.imshow("Result", result)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run(1)
    # This above line will js allow me to test the object counter without having to click the button in the GUI. I can change the number to test different colours (1=Red, 2=Green, 3=Blue).