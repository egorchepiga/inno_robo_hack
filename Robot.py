import numpy as np
import cv2 as cv
import socket

class Robot:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT

        self.left_cap = cv.VideoCapture('http://10.127.50.72:801')
        self.right_cap = cv.VideoCapture('http://10.127.50.72:800')

        self.bm = cv.StereoSGBM_create(
            blockSize=3, numDisparities=96,
            P1=305, P2=2048, mode=cv.StereoSGBM_MODE_HH)

        self.me = {
                'head': {
                    'yaw': 0,
                    'pitch': 0,
                    'roll': 0
                },
                'torso': {
                    'yaw': 0,
                    'pitch': 0,
                    'roll': 0
                },
                'shoulder_L': {
                    'yaw': 0,
                    'pitch': 0,
                    'roll': 0
                },
                'shoulder_R': {
                    'yaw': 0,
                    'pitch': 0,
                    'roll': 0
                }
        }

        self.start_socket_shit()


    def start_socket_shit(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.HOST, self.PORT))
        print('socket shit enabled')


    def send_msg(self, msg):
        print('senf msg {}'.format(msg))
        response = ''
        i = 0
        while len(response) <= 1:
            self.s.send(bytes(msg + '\n\r', 'ASCII'))
            response = self.s.recv(1024)
            print(i, end='\r')
            i += 1
            if i > 1000:
                break
        print('get response')
        return response


    def rotate_shoulder_R(self, yaw=0, pitch=0, roll=0, absolute=False):
        if absolute == True:
            self.me['shoulder_R']['yaw'] = 0
            self.me['shoulder_R']['pitch'] = 0
            self.me['shoulder_R']['roll'] = 0

        self.me['shoulder_R']['yaw'] += yaw
        self.me['shoulder_R']['pitch'] += pitch
        self.me['shoulder_R']['roll'] += roll

        msg = 'ROBOT:MOTORS:R.ShoulderR:POSSET:{}'.format(self.me['shoulder_R']['yaw'])
        self.send_msg(msg)

        msg = 'ROBOT:MOTORS:R.ShoulderF:POSSET:{}'.format(self.me['shoulder_R']['pitch'])
        self.send_msg(msg)

        msg = 'ROBOT:MOTORS:R.ShoulderS:POSSET:{}'.format(self.me['shoulder_R']['roll'])
        self.send_msg(msg)

        print(self.me)


    def rotate_shoulder_L(self, yaw=0, pitch=0, roll=0, absolute=False):
        if absolute == True:
            self.me['shoulder_L']['yaw'] = 0
            self.me['shoulder_L']['pitch'] = 0
            self.me['shoulder_L']['roll'] = 0

        self.me['shoulder_L']['yaw'] += yaw
        self.me['shoulder_L']['pitch'] += pitch
        self.me['shoulder_L']['roll'] += roll

        msg = 'ROBOT:MOTORS:L.ShoulderR:POSSET:{}'.format(self.me['shoulder_L']['yaw'])
        self.send_msg(msg)

        msg = 'ROBOT:MOTORS:L.ShoulderF:POSSET:{}'.format(self.me['shoulder_L']['pitch'])
        self.send_msg(msg)

        msg = 'ROBOT:MOTORS:L.ShoulderS:POSSET:{}'.format(self.me['shoulder_L']['roll'])
        self.send_msg(msg)

        print(self.me)


    def rotate_torso(self, yaw=0, pitch=0, roll=0, absolute=False):
        if absolute == True:
            self.me['torso']['yaw'] = 0
            self.me['torso']['pitch'] = 0
            self.me['torso']['roll'] = 0

        self.me['torso']['yaw'] += yaw
        self.me['torso']['pitch'] += pitch
        self.me['torso']['roll'] += roll

        msg = 'ROBOT:MOTORS:TorsoR:POSSET:{}'.format(self.me['torso']['yaw'])
        self.send_msg(msg)

        msg = 'ROBOT:MOTORS:TorsoF:POSSET:{}'.format(self.me['torso']['pitch'])
        self.send_msg(msg)

        msg = 'ROBOT:MOTORS:TorsoS:POSSET:{}'.format(self.me['torso']['roll'])
        self.send_msg(msg)

        print(self.me)


    def rotate_head(self, yaw=0, pitch=0, roll=0, absolute=False):
        if absolute == True:
            self.me['head']['yaw'] = 0
            self.me['head']['pitch'] = 0
            self.me['head']['roll'] = 0

        self.me['head']['yaw'] += yaw
        self.me['head']['pitch'] += pitch
        self.me['head']['roll'] += roll

        msg = 'ROBOT:MOTORS:HeadR:POSSET:{}'.format(self.me['head']['yaw'])
        self.send_msg(msg)

        msg = 'ROBOT:MOTORS:HeadF:POSSET:{}'.format(self.me['head']['pitch'])
        self.send_msg(msg)

        msg = 'ROBOT:MOTORS:HeadS:POSSET:{}'.format(self.me['head']['roll'])
        self.send_msg(msg)

        print(self.me)


    def get_sensor_data(self):
        ret_left, left_frame = self.left_cap.read()
        ret_right, right_frame = self.right_cap.read()

        if not (ret_left and ret_right):
            raise BaseException('Suka, some shit with cameras')

        disp = self.bm.compute(left_frame, right_frame)
        f = 2.7465
        T = 0.1
        Q = np.float32([
            [1, 0, 0, -disp.shape[1]//2],
            [0, 1, 0, -disp.shape[0]//2],
            [0, 0, 0, f],
            [0, 0, -1/T, 0],
        ])

        XYZ = cv.reprojectImageTo3D(disp, Q)
        disp = disp.astype(np.float32) / 16.0

        mask_brown = cv.inRange(left_frame, (40, 40, 40), (90, 90, 90))
        mask_brown = cv.morphologyEx(mask_brown, cv.MORPH_OPEN, np.ones((5, 5), dtype=np.uint8))

        mask_chess = cv.inRange(left_frame, (0, 0, 0), (50, 50, 50))
        mask_chess = cv.morphologyEx(mask_chess, cv.MORPH_OPEN, np.ones((5, 5), dtype=np.uint8))

        return {
            'left': left_frame,
            'right': right_frame,
            'disp': disp,
            'XYZ': XYZ,
            'mask_brown': mask_brown,
            'mask_chess': mask_chess,
        }


