import utils


class Elbow:
    def __init__(self, side, socket):
        self.socket = socket
        self.side = side

    def fold(self, degree):
        msg = "ROBOT:MOTORS:{}.Elbow:POSSET:{}".format(self.side, str(degree))
        response = utils.send_msg(msg, self.socket)
        print(response)
        return response

    def rotation(self, degree):
        msg = "ROBOT:MOTORS:{}.ElbowR:POSSET:{}".format(self.side, str(degree))
        response = utils.send_msg(msg, self.socket)
        print(response)
        return response
