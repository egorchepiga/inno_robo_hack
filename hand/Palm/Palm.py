import hand.Palm.Finger


class Palm:

    def __init__(self, side, socket):
        self.thumb = hand.Palm.Finger.Finger(side, "Thumb", socket)
        self.index = hand.Palm.Finger.Finger(side, "Index", socket)
        self.middle = hand.Palm.Finger.Finger(side, "Middle", socket)
        self.ring = hand.Palm.Finger.Finger(side, "Ring", socket)
        self.little = hand.Palm.Finger.Finger(side, "Little", socket)
