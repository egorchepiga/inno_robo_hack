import utils


class Neck:
    def __init__(self, socket):
        self.socket = socket

    def tilt(self, degree):
        msg = "ROBOT:MOTORS:{}.Neck:POSSET:{}".format(self.side, str(degree))
        response = utils.send_msg(msg, self.socket)
        print(response)
        return response