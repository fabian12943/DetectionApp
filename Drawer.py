import mediapipe as mp

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils


class Drawer:

    @staticmethod
    def draw_pose(image, landmark_list, connections=True, display=True):
        output_image = image.copy()

        if display:
            mp_draw.draw_landmarks(image, landmark_list, mp_pose.POSE_CONNECTIONS if connections else None)
            return image
        else:
            mp_draw.draw_landmarks(output_image, landmark_list, mp_pose.POSE_CONNECTIONS if connections else None)
            return output_image
