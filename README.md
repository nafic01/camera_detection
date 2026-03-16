## Project Overview

This project is for a 5-day work experience with a robotics company. The goal is to create a simple computer vision program using Python that can detect and count objects of a chosen colour using a laptop webcam.

By the end of the project, the program can:

* Open your webcam
* Detect objects of a specific colour
* Draw rectangles around each detected object
* Display the number of objects detected in real-time
* Use mediapipe to detect hands

Computer vision is widely used in robotics, automation, and AI systems to help machines understand their surroundings. This project introduces the basics of object detection and counting.

---

## Tools Used
* **Python** - I am using Python 3.14
* **OpenCV** – for labelling and detecting objects using the webcam
* **NumPy** – for numerical operations with OpenCV
* **GitHub** – for version control and progress tracking
* **Mediapipe** - for detecting hand gestures
* Laptop with webcam

You can install the required libraries with:

```bash
pip3 install opencv-python numpy mediapipe
```


---

## Project Structure

```
GestureVision
│
├── object_counter.py       # Final program for object detection and counting
├── main.py                 # Brings together all the files and provides the GUI using TKinter
├── handtracker.py          # Final program for hand detection
├── README.md               # Project documentation
```

---

## How to Run the Program

1. Clone the repository:

```bash
git clone https://github.com/nafic01/GestureVision
```

2. Navigate to the project folder:


3. Run the GUI program:

```bash
python main.py
```

Press `q` to close the webcam window.

