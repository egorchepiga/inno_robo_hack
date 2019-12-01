import utils


class Wrist:
    def __init__(self, side, socket):
        self.socket = socket
        self.side = side

    def front(self, degree):
        msg = "ROBOT:MOTORS:{}.WristF:POSSET:{}".format(self.side, str(degree))
        response = utils.send_msg(msg, self.socket)
        print(response)
        return response

    def side(self, degree):
        msg = "ROBOT:MOTORS:{}.WristS:POSSET:{}".format(self.side, str(degree))
        response = utils.send_msg(msg, self.socket)
        print(response)
        return response

    def rotate(self, degree):
        msg = "ROBOT:MOTORS:{}.WristR:POSSET:{}".format(self.side, str(degree))
        response = utils.send_msg(msg, self.socket)
        print(response)
        return response
