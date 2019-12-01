import utils


class Finger:
    def __init__(self, side, finger, socket):
        self.side = side
        self.socket = socket
        self.finger = finger

    def fold(self, degree):
        msg = "ROBOT:MOTORS:{}.Finger.{}:POSSET:{}".format(self.side, self.finger, str(degree))
        response = utils.send_msg(msg, self.socket)
        print(response)
        return response

    def rotate(self, degree):
        msg = "ROBOT:MOTORS:{}.Finger.{}S:POSSET:{}".format(self.side, self.finger, str(degree))
        response = utils.send_msg(msg, self.socket)
        print(response)
        return response

