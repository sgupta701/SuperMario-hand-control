import cv2
import mediapipe as mp
import pyautogui
import time  

# Gesture functions with higher thresholds
def thumb_left(hand_landmarks, threshold=0.1): 
    thumb_tip = hand_landmarks.landmark[4]
    wrist = hand_landmarks.landmark[0]
    if thumb_tip.x < wrist.x - threshold:
        if abs(thumb_tip.y - wrist.y) > 0.02:
            return True
    return False

def pinky_right(hand_landmarks, threshold=0.1): 
    pinky_tip = hand_landmarks.landmark[20]
    wrist = hand_landmarks.landmark[0]
    if pinky_tip.x > wrist.x + threshold:
        pinky_dip = hand_landmarks.landmark[18]
        if pinky_tip.y < pinky_dip.y:
            return True
    return False

def index_up(hand_landmarks):
    index_tip = hand_landmarks.landmark[8]
    index_pip = hand_landmarks.landmark[6]
    if index_tip.y < index_pip.y:
        return True
    return False

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)

cv2.namedWindow("Hand Tracking", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Hand Tracking", 320, 240)  # smaller window

keys_pressed = set()

gesture_start_times = {}
debounce_delay = 0.3 

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read from camera.")
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    current_keys = set()

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            gestures = {
                'a': thumb_left(hand_landmarks),
                'd': pinky_right(hand_landmarks),
                'space': index_up(hand_landmarks)
            }

            for key, detected in gestures.items():
                if detected:
                    now = time.time()
                    if key not in gesture_start_times:
                        gesture_start_times[key] = now
                    elif now - gesture_start_times[key] >= debounce_delay:
                        current_keys.add(key)
  
                    if key == 'a':
                        cv2.putText(img, 'Move Left (A)', (10, 70), cv2.FONT_HERSHEY_SIMPLEX,
                                    1, (255, 0, 0), 2)
                    elif key == 'd':
                        cv2.putText(img, 'Move Right (D)', (10, 120), cv2.FONT_HERSHEY_SIMPLEX,
                                    1, (0, 255, 0), 2)
                    elif key == 'space':
                        cv2.putText(img, 'Jump (Space)', (10, 170), cv2.FONT_HERSHEY_SIMPLEX,
                                    1, (0, 0, 255), 2)
                else:
                    if key in gesture_start_times:
                        del gesture_start_times[key]

    for key in current_keys:
        if key not in keys_pressed:
            pyautogui.keyDown(key)

    for key in keys_pressed:
        if key not in current_keys:
            pyautogui.keyUp(key)

    keys_pressed = current_keys

    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.08)  


for key in keys_pressed:
    pyautogui.keyUp(key)

cap.release()
cv2.destroyAllWindows()
