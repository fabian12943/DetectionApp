from Hand import Hand


class LeftHand(Hand):

    def __init__(self, detection_results, landmarks):
        super().__init__(detection_results, landmarks)
