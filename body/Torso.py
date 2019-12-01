import utils


class Torso:
    def __init__(self, socket):
        self.socket = socket

    def rotate(self, degree):
        msg = "ROBOT:MOTORS:{}.TorsoR:POSSET:{}".format(self.side, str(degree))
        response = utils.send_msg(msg, self.socket)
        print(response)
        return response

    def move(self, degree):
        msg = "ROBOT:MOTORS:{}.TorsoS:POSSET:{}".format(self.side, str(degree))
        response = utils.send_msg(msg, self.socket)
        print(response)
        return response

    def tilt(self, degree):
        msg = "ROBOT:MOTORS:{}.TorsoF:POSSET:{}".format(self.side, str(degree))
        response = utils.send_msg(msg, self.socket)
        print(response)
        return response
