import cv2
import mediapipe as mp
import pyautogui
import math

# MediaPipe elleri başlat
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Ekran boyutları
screen_width, screen_height = pyautogui.size()

# Mesafe hesaplama
def distance(point1, point2):
    return math.hypot(point2[0] - point1[0], point2[1] - point1[1])

# Tıklama eşik değeri
CLICK_THRESHOLD = 30

# Kamera
cap = cv2.VideoCapture(0)

with mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7) as hands:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            continue

        frame = cv2.flip(frame, 1)  # Aynalama
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)

        if result.multi_hand_landmarks and result.multi_handedness:
            for hand_landmarks, handedness in zip(result.multi_hand_landmarks, result.multi_handedness):
                hand_label = handedness.classification[0].label  # 'Left' veya 'Right'

                # Landmarkları al
                landmarks = hand_landmarks.landmark
                h, w, _ = frame.shape

                if hand_label == "Right":
                    # Sağ el: imleç kontrolü
                    index_tip = landmarks[8]
                    x = int(index_tip.x * w)
                    y = int(index_tip.y * h)

                    screen_x = int(index_tip.x * screen_width)
                    screen_y = int(index_tip.y * screen_height)

                    pyautogui.moveTo(screen_x, screen_y)
                    cv2.circle(frame, (x, y), 10, (255, 0, 0), -1)

                elif hand_label == "Left":
                    # Sol el: tıklama işlemleri
                    thumb_tip = landmarks[4]
                    index_tip = landmarks[8]
                    index_pip = landmarks[6]
                    pinky_tip = landmarks[20]

                    # Koordinatlara çevir
                    thumb = (int(thumb_tip.x * w), int(thumb_tip.y * h))
                    index = (int(index_tip.x * w), int(index_tip.y * h))
                    index2 = (int(index_pip.x * w), int(index_pip.y * h))
                    pinky = (int(pinky_tip.x * w), int(pinky_tip.y * h))

                    # Mesafeleri ölç
                    dist_single_click = distance(thumb, index)
                    dist_double_click = distance(thumb, index2)
                    dist_right_click = distance(thumb, pinky)

                    if dist_single_click < CLICK_THRESHOLD:
                        pyautogui.click()
                        cv2.putText(frame, "Left Click", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    elif dist_double_click < CLICK_THRESHOLD:
                        pyautogui.doubleClick()
                        cv2.putText(frame, "Double Click", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                    elif dist_right_click < CLICK_THRESHOLD:
                        pyautogui.rightClick()
                        cv2.putText(frame, "Right Click", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                # Landmarkları çiz
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('El Kontrolu', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
