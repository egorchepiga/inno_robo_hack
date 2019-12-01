import utils


class Head:
    def __init__(self, socket):
        self.socket = socket

        self.position = {
            'yaw': 0,
            'pitch': 0,
            'roll': 0
        }

    def tilt(self, degree):
        msg = "ROBOT:MOTORS:HeadF:POSSET:{}".format(str(degree))
        response = utils.send_msg(msg, self.socket)
        print(response)
        return response

    def shake(self, degree):
        msg = "ROBOT:MOTORS:HeadS:POSSET:{}".format(str(degree))
        response = utils.send_msg(msg, self.socket)
        print(response)
        return response

    def rotate(self, degree):
        msg = "ROBOT:MOTORS:HeadR:POSSET:{}".format(str(degree))
        response = utils.send_msg(msg, self.socket)
        print(response)
        return response