# 🖐️ Hand Gesture Controlled Mario Movement 🎮

This project lets you **control Mario using hand gestures** detected via your webcam. By combining **MediaPipe** for gesture recognition and **PyAutoGUI** for key simulation, you can move Mario left, right, or make him jump—**without touching your keyboard!**

---

## 📹 Demo

> Raise your hand and control Mario:
- 👈 **Thumb Left** → Move Left (`A`)
- 👉 **Pinky Right** → Move Right (`D`)
- ☝️ **Index Up** → Jump (`Space`)

---

## 🛠️ Technologies Used

| Library       | Purpose                                  |
|---------------|------------------------------------------|
| OpenCV        | Webcam capture and image display         |
| MediaPipe     | Real-time hand landmark detection        |
| PyAutoGUI     | Simulates keyboard input to control Mario|
| Time          | Debouncing and gesture throttling        |

---

## ✅ Features

- Real-time hand gesture recognition via webcam
- Keyboard control using PyAutoGUI
- Visual gesture feedback on OpenCV window
- Adjustable gesture sensitivity and debounce
- Loop throttling for **smooth and slower** movement

---

## 📁 File Structure

```
mario-hand-control/
├── hand_tracking.py         # Main script
├── requirements.txt         # Dependencies
├── README.md  
```

---

## 🧑‍💻 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/sgupta701/SuperMario-hand-control.git
cd mario-hand-control
```

### 2. Install Dependencies

```bash
pip install pillow pygetwindow mouseinfo pyrect pymsgbox
pip install opencv-python mediapipe pyautogui
```

### 3. Run the Script

```bash
python hand_gesture_mario.py
```

---

## 🎮 Gesture Controls

| Gesture             | Action          | Key Pressed |
|---------------------|------------------|-------------|
| Thumb to the Left   | Move Left        | `A`         |
| Pinky to the Right  | Move Right       | `D`         |
| Index Finger Raised | Jump             | `Space`     |

---

## 🧠 How It Works

1. **MediaPipe** detects 21 hand landmarks using a webcam feed.
2. Custom functions analyze gesture geometry:
   - Thumb x-position for "left"
   - Pinky x/y-position for "right"
   - Index y-position for "jump"
3. Detected gestures trigger simulated key presses via **PyAutoGUI**.
4. A **debounce timer** prevents accidental rapid triggers.
5. A `time.sleep(0.08)` call slows down the main loop so Mario moves more naturally.

---


## 🙌 Credits

- [MediaPipe by Google](https://github.com/google/mediapipe)
- [PyAutoGUI by Al Sweigart](https://pyautogui.readthedocs.io/)
- [OpenCV Library](https://opencv.org/)

---

> 🎉 Enjoy playing Mario using just your hand gestures!
