# 🖱️ Hand Gesture-Based Virtual Mouse

This project allows you to control your computer mouse using **hand gestures** detected from a webcam.  
It uses **OpenCV**, **MediaPipe**, and **PyAutoGUI** to recognize hand landmarks and trigger mouse actions in real time.

---

## 🚀 Features

- Move cursor with right-hand index finger  
- Perform **left click** gesture  
- Perform **double click** gesture  
- Perform **right click** gesture  
- Real-time hand tracking (MediaPipe Hands)  
- Multi-hand support with gesture recognition  
- Natural and intuitive camera-based interaction

---

## 🧠 Technologies Used

- Python 3  
- OpenCV  
- MediaPipe  
- PyAutoGUI  
- NumPy  

---

## 📁 Project Structure
```
hand-gesture-virtual-mouse/
│
├── src/
│ ├── el_mouse_kontrol.py  # Main file: cursor control + gesture actions
│ ├── el_tespiti.py        # Hand detection functions
│ └── kamera_test.py       # Webcam testing script
│
├── docs/
│ ├── Mouse.png
│ ├── Left Click.png
│ └── Double Click.png
│
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Install dependencies:
pip install -r requirements.txt

### 2. Run the application:
python src/el_mouse_kontrol.py

 Press Q to exit.

## 📝 Future Improvements

- Gesture-based scrolling
- More stable fingertip tracking
- Improved click detection logic
- Configuration GUI (sensitivity, camera selection)

## 👤 Author

**Hatice Sude Mutlu**  
Computer Engineering Student  
GitHub: https://github.com/HaticeSude