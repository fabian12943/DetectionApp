import mediapipe as mp
import cv2

from LeftHand import LeftHand
from RightHand import RightHand


class HandDetector:

    def __init__(self, static_image_mode=False, max_num_hands=2,
                 min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.static_image_mode = static_image_mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.static_image_mode, self.max_num_hands,
                                         self.min_detection_confidence, self.min_tracking_confidence)

    def process(self, image):
        # Flip image as handedness assumes the input to be mirrored
        image = cv2.flip(image, 1)

        # Convert image from BGR to RGB format to perform landmarks detection
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Perform the hands landmarks detection
        results = self.hands.process(image_rgb)

        # Check if any landmarks were found in the frame
        if results.multi_hand_landmarks:
            hands = []
            for hand_no in range(0, len(results.multi_hand_landmarks)):
                # Detect landmarks of current hand
                landmarks = []
                for _, landmark in enumerate(results.multi_hand_landmarks[hand_no].landmark):
                    height, width, _ = image_rgb.shape
                    cx, cy, cz = int(landmark.x * width), int(landmark.y * height), int(landmark.z * width)
                    landmarks.append({'cx': cx, 'cy': cy, 'cz': cz})

                # Detect if current hand is left or right hand
                classification = results.multi_handedness[hand_no].classification[0]

                # Initialize hand object depending on hand side
                if classification.label == "Right":
                    hands.append(RightHand(results.multi_hand_landmarks[hand_no], landmarks))
                if classification.label == "Left":
                    hands.append(LeftHand(results.multi_hand_landmarks[hand_no], landmarks))

            return hands
