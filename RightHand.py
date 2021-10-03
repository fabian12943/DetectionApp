from Hand import Hand


class RightHand(Hand):

    def __init__(self, detection_results, landmarks):
        super().__init__(detection_results, landmarks)
