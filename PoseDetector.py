import mediapipe as mp
import cv2

from Pose import Pose


class PoseDetector:
    def __init__(self, static_image_mode=False, model_complexity=1, smooth_landmarks=True, enable_segmentation=False,
                 smooth_segmentation=True, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.static_image_mode = static_image_mode
        self.model_complexity = model_complexity
        self.smooth_landmarks = smooth_landmarks
        self.enable_segmentation = enable_segmentation
        self.smooth_segmentation = smooth_segmentation
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(self.static_image_mode, self.model_complexity, self.smooth_landmarks,
                                      self.enable_segmentation, self.smooth_segmentation,
                                      self.min_detection_confidence, self.min_tracking_confidence)

    def process(self, image):
        # Convert image from BGR to RGB format to perform landmarks detection
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Perform the pose landmarks detection
        results = self.pose.process(image_rgb)

        # Check if any landmarks were found in the frame
        if results.pose_landmarks:
            landmarks = []
            for _, landmark in enumerate(results.pose_landmarks.landmark):
                height, width, _ = image.shape
                cx, cy, cz = int(landmark.x * width), int(landmark.y * height), int(landmark.z * width)
                landmarks.append({'cx': cx, 'cy': cy, 'cz': cz, 'visibility': landmark.visibility})

            return Pose(results, landmarks)
