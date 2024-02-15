# Hand Gesture Recognizer

import serial
import time
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense
from keras.models import Sequential, load_model

# Arduino Received commands
FORWARD = 'F'
BACKWARD = 'B'
LEFT = 'L'
RIGHT = 'R'
FORWARD_LEFT = 'G'
FORWARD_RIGHT = 'I'
BACK_LEFT = 'H'
BACK_RIGHT = 'J'
STOP = 'S'

# Create a serial object
arduino = serial.Serial('COM6', 9600)

def send_command(command):
    # Encode the command as bytes and send it
    arduino.write(command.encode())
    time.sleep(0.015)  # Allow some time for the command to be processed

# Initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model = load_model('mp_hand_gesture')

# Load class names
with open('gesture.names', 'r') as f:
    classNames = f.read().split('\n')

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read each frame from the webcam
    _, frame = cap.read()

    x, y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get hand landmark prediction
    result = hands.process(framergb)

    className = ''

    # post process the result
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])

            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            # Predict gesture
            prediction = model.predict([landmarks])
            classID = np.argmax(prediction)
            className = classNames[classID]
 

    # Show the prediction on the frame
    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 122, 255), 2, cv2.LINE_AA)

    if className == 'okay':
        send_command('F')  # Forward
    elif className == 'stop':
        send_command('B')  # Backward
    elif className == 'fist':
        send_command('L')  # Left
    elif className == 'peace':
        send_command('R')  # Right
    else:
        send_command("stop")  # No movement

    # Show the final output
    cv2.imshow("Output", frame) 

    if cv2.waitKey(1) == ord('q'):
        break

# Release the webcam and close all active windows
cap.release()
cv2.destroyAllWindows()