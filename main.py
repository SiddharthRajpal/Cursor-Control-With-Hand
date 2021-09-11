import os
try:
    import pyautogui
except:
    os.system("pip install pyautogui")
    print(" Missing Library : PyAutoGUI \n Installing Required Library")

try:
    import mediapipe as mp
except:
    pyautogui.alert(" Missing Library : Mediapipe \n Installing Required Libraries", title="Installing Mediapipe")
    os.system("pip install mediapipe")

try:
    import cv2 as cv
except:
    os.system("pip install opencv-python")
    pyautogui.alert(" Missing Library : OpenCV \n Installing Required Libraries", title="Installing OpenCV")

    import time
    import os
    import math

confirm = pyautogui.confirm(
    'Running This Program Can Cause Extreme frutration and cause you to yeet your cat.... are you sure you want to run this?',
    title="Warning ⚠ ")
mp_draw = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


def calculateDistance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


cap = cv.VideoCapture(1)  # Change this to 0 if it gives error in cv.cvtColor
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while True:
        if confirm == "OK":
            pass
        else:
            break
        ret, frame = cap.read()
        image = cv.cvtColor(cv.flip(frame, 1), cv.COLOR_BGR2RGB)
        # print("Never Gonna Give You Up")
        image.flags.writeable = False
        result = hands.process(image)
        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        # print(result.multi_hand_landmarks)
        width, height, color = image.shape
        if result.multi_hand_landmarks:
            # autopy.alert.alert("Warning... Hand Detected, stop now",title = "Hand Error")
            for num, hand in enumerate(result.multi_hand_landmarks):
                mp_draw.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)
                xindex1 = hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * width + 60
                xindex1 = int(xindex1)
                yindex1 = hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height - 70
                yindex1 = int(yindex1)
                z = hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].z
                #print(hand.landmark[mp_hands.HandLandmark.THUMB_TIP].x)
                xthumb = hand.landmark[mp_hands.HandLandmark.THUMB_TIP].x
                #print(type (result.multi_hand_landmarks))
                #print(result.multi_hand_landmarks)
                #print(len(result.multi_hand_landmarks))
                if len(result.multi_hand_landmarks) > 1:
                    pyautogui.click()
                    #print("Something")
                else:
                    pass

                try:
                    pyautogui.moveTo(xindex1 * 5, yindex1 * 5)
                except:
                    pass

                # cv.circle(image, (xindex1,yindex1),100,thickness=1000,color=(255,255,255))
        cv.imshow("Result", image)
        if cv.waitKey(1) & 0xFF == ord("q"):
            break
cv.destroyAllWindows()
cap.release()
