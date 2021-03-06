import cv2
from time import time

from PoseDetector import PoseDetector


class App:

    __conf = {
        "INPUT_LOCATION": 0,
        "CAP_WIDTH": 1280,
        "CAP_HEIGHT": 720,
        "DISPLAY_OUTPUT_IMAGE": True,
        "SHOW_FPS": True
    }

    __setters = ["INPUT_LOCATION", "CAP_WIDTH", "CAP_HEIGHT", "DISPLAY_OUTPUT_IMAGE", "SHOW_FPS"]

    @staticmethod
    def config(name):
        return App.__conf[name]

    @staticmethod
    def set(name, value):
        if name in App.__setters:
            App.__conf[name] = value
        else:
            raise NameError("Name not accepted in set() method")


def main():
    cap = cv2.VideoCapture(App.config("INPUT_LOCATION"))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, App.config("CAP_WIDTH"))
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, App.config("CAP_HEIGHT"))

    if not cap.isOpened():
        print('Cannot open camera! Exiting...')
        exit()

    # Time of last processed frame
    prev_frame_time = 0

    pose_detector = PoseDetector(min_detection_confidence=0.8, min_tracking_confidence=0.8)

    while True:
        # Capture video input frame-by-frame
        success, image_bgr = cap.read()

        # Check if frame was read correctly
        if not success:
            print("Can't receive frame. Exiting...")
            break

        # Check frame for pose
        pose = pose_detector.process(image_bgr)

        if pose is not None:
            pose.draw_landmarks(image_bgr)

        # Flip the frame horizontally for natural (selfie-view) visualization
        image_bgr = cv2.flip(image_bgr, 1)

        if App.config("SHOW_FPS"):
            # Time of current processed frame
            curr_frame_time = time()

            # Check if the difference between the previous and current frame is > 0 to avoid division by zero
            if (curr_frame_time - prev_frame_time) > 0:

                # Calculate the number of frames per second
                fps = 1.0 / (curr_frame_time - prev_frame_time)

                # Write the calculated number of fps on the image
                cv2.putText(image_bgr, 'FPS: {}'.format(int(fps)), (10, 30),
                            cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1)

            # Update the previous frame time to current frame time
            prev_frame_time = curr_frame_time

        # Display the resulting frame
        cv2.imshow("App", image_bgr)
        if cv2.waitKey(1) == ord('q'):
            break

    # Release capture when done
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
