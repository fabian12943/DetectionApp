import mediapipe as mp

from Drawer import Drawer


class Pose:

    # MediaPipe Pose
    mp_pose = mp.solutions.pose

    def __init__(self, detection_results, landmarks):
        self.detection_results = detection_results
        self.landmarks = landmarks

    def draw_landmarks(self, image, connections=True, display=True):
        landmark_list = self.detection_results.pose_landmarks

        return Drawer.draw_landmarks(image, landmark_list,
                                     self.mp_pose.POSE_CONNECTIONS if connections else None, display)
