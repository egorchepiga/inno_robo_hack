import socket
from utils import send_msg

from hand.Hand import Hand
from body.Head import Head
from body.Neck import Neck
from body.Torso import Torso


class Robot:

    def __init__(self, HOST, PORT):

        self.HOST = HOST
        self.PORT = PORT

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.HOST, self.PORT))

        self.hand = Hand(self.socket)
        self.head = Head(self.socket)
        self.neck = Neck(self.socket)
        self.torso = Torso(self.socket)

    def rotate_head(self, yaw=0, pitch=0, roll=0, absolute=False):
        if absolute:
            self.head['yaw'] = 0
            self.head['pitch'] = 0
            self.head['roll'] = 0
        self.head['yaw'] += yaw
        self.head['pitch'] += pitch
        self.head['roll'] += roll

        msg = 'ROBOT:MOTORS:HeadR:POSSET:{}'.format(self.head['yaw'])
        send_msg(self.socket, msg)

        msg = 'ROBOT:MOTORS:HeadF:POSSET:{}'.format(self.head['pitch'])
        send_msg(self.socket, msg)

        msg = 'ROBOT:MOTORS:HeadS:POSSET:{}'.format(self.head['roll'])
        send_msg(self.socket, msg)

        print(self.head)

    def get_list(self):
        msg = 'ROBOT:MOTORS:LIST'
        response = send_msg(self.socket, msg)
        print(response)

