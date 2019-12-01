import utils


class Shoulder:
    def __init__(self, side, socket):
        self.socket = socket
        self.side = side

    def front(self, degree):
        msg = "ROBOT:MOTORS:{}.ShoulderF:POSSET:{}".format(self.side, str(degree))
        response = utils.send_msg(msg, self.socket)
        print(response)
        return response

    def side(self, degree):
        msg = "ROBOT:MOTORS:{}.ShoulderS:POSSET:{}".format(self.side, str(degree))
        response = utils.send_msg(msg, self.socket)
        print(response)
        return response

