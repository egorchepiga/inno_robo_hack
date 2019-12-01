import numpy as np
import cv2 as cv

from Robot import Robot
from automotive import *

HOST = '10.127.50.72'
PORT = 10099

Fred = Robot(HOST,PORT)


while True:
    sensors_data = Fred.get_sensor_data()
    left, right, disp = sensors_data['left'], sensors_data['right'], sensors_data['disp']
    mask_brown, mask_chess = sensors_data['mask_brown'], sensors_data['mask_chess']
    XYZ = sensors_data['XYZ']

    Z = XYZ[..., 2]
    Z = Z.astype(np.uint8)
    cv.imshow('disp', cv.applyColorMap(disp.astype(np.uint8), cv.COLORMAP_RAINBOW))

    
    cv.imshow('stacked', np.hstack((left, right)))

    key = cv.waitKey(10)
    try:
        if key == ord('q'):
            break
        elif key == ord('a'):
            Fred.rotate_head(yaw=5)
        elif key == ord('d'):
            Fred.rotate_head(yaw=-5)
        elif key == ord('s'):
            Fred.rotate_head(pitch=5)
        elif key == ord('w'):
            Fred.rotate_head(pitch=-5)
        elif key == ord('0'):
            watch_on_zero(Fred)
        elif key == ord('9'):
            watch_on_target(Fred)
        elif key == ord('8'):
            watch_on_box(Fred)
        elif key == ord('7'):
            test(Fred)
    except BrokenPipeError:
        print('broken pipe')
        Fred.start_socket_shit()

