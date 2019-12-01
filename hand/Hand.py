from hand.Shoulder import Shoulder
from hand.Elbow import Elbow
from hand.Wrist import Wrist
from hand.Palm.Palm import Palm


class Hand:

    def __init__(self, socket):
        self.right = self.Side("R", self.socket)
        self.left = self.Side("L", self.socket)
        self.socket = socket

    class Side:
        def __init__(self, side, socket):
            self.a = 0
            self.shoulder = Shoulder(side, socket)
            self.elbow = Elbow(side, socket)
            self.wrist = Wrist(side, socket)
            self.palm = Palm(side, socket)
