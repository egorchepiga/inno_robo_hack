import numpy as np

from Robot import Robot
from automotive import *

HOST = '10.127.50.72'
PORT = 10099

Fred = Robot(HOST, PORT)

while True:
    sensors_data = Fred.get_sensor_data()
    left, right, disp = sensors_data['left'], sensors_data['right'], sensors_data['disp']

    disp = disp.astype(np.uint8)
    cv.imshow('disp', cv.applyColorMap(disp, cv.COLORMAP_RAINBOW))

    cv.imshow('stacked', np.hstack((left, right)))

    key = cv.waitKey(25)
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
        elif key == ord('p'):
            watch_on_target(Fred)
        elif key == ord('o'):
            watch_on_box(Fred)
    except BrokenPipeError:
        print('broken pipe')
        Fred.start_socket_shit()

