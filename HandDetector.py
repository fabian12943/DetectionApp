import cv2
import mediapipe as mp
import time


class HandDetector:

    def __init__(self, static_image_mode=False, max_num_hands=2,
                 min_detection_confidence=0.60, min_tracking_confidence=0.65):
        self.static_image_mode = static_image_mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.static_image_mode, self.max_num_hands,
                                         self.min_detection_confidence, self.min_tracking_confidence)
        self.mp_draw = mp.solutions.drawing_utils
        self.results = None

    def find_hands(self, img, imgOut, draw=False):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(imgOut, handLms, self.mp_hands.HAND_CONNECTIONS)

        return imgOut

    def get_position(self, img, draw=False):
        landmark_list = []

        if self.results.multi_hand_landmarks:
            for hand_number in range(0, len(self.results.multi_hand_landmarks)):
                classification = self.results.multi_handedness[hand_number].classification[0]
                landmark_list.append([[classification.label, classification.score], []])
                hand_landmarks = self.results.multi_hand_landmarks[hand_number]
                for hand_id, hand_landmark in enumerate(hand_landmarks.landmark):
                    h, w, c = img.shape
                    cx, cy = int(hand_landmark.x * w), int(hand_landmark.y * h)
                    landmark_list[hand_number][1].append([hand_id, cx, cy])
                if draw:
                    cv2.putText(img, classification.label, (int(landmark_list[hand_number][1][0][1]),
                                                            int(landmark_list[hand_number][1][0][2])),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 2)

        return landmark_list
