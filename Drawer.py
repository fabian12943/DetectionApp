import mediapipe as mp

mp_draw = mp.solutions.drawing_utils


class Drawer:

    @staticmethod
    def draw_landmarks(image, landmark_list, connections, display=True):
        output_image = image.copy()

        if display:
            mp_draw.draw_landmarks(image, landmark_list, connections)
            return image
        else:
            mp_draw.draw_landmarks(output_image, landmark_list, connections)
            return output_image
