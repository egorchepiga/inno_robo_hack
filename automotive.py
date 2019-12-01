import time
import numpy as np
import cv2 as cv


def watch_on_zero(fedor):
    print('watch on zero sequence')
    try:
        fedor.rotate_head(0, 0, 0, absolute=True)
    except BrokenPipeError:
        print('broken pipe')
        fedor.start_socket_shit()
        watch_on_zero(fedor)


def watch_on_target(fedor):
    print('watch on target sequence')
    try:
        # fedor.rotate_head(30, 20, 0, absolute=True)
        fedor.rotate_head(0, 20, 0, absolute=True)
        fedor.rotate_torso(0, 30, 0, absolute=True)
        time.sleep(5)
        sensors_data = fedor.get_sensor_data()
        left, right, disp = sensors_data['left'], sensors_data['right'], sensors_data['disp']
        mask_brown, mask_chess = sensors_data['mask_brown'], sensors_data['mask_chess']

        disp = disp.astype(np.uint8)

        roi_left_disp = cv.bitwise_and(cv.inRange(disp, 10, 96), mask_chess)
        roi_left_disp[:,:390] = 0
        roi_left_disp[:,500:] = 0
        roi_right_disp = cv.bitwise_and(cv.inRange(disp, 70, 96), mask_brown)

        number = 0

        y_coords = np.where(roi_left_disp > 0)[1]
        if len(y_coords) > 0:
            print(y_coords.min(), y_coords.mean(), y_coords.max())
            mean = y_coords.mean()
            if 455 < mean < 470:
                number = 1
            elif 470 < mean < 485:
                number = 2
            elif 485 < mean < 550:
                number = 3
        else:
            print('no target')

        print('Number:', number)

    except BrokenPipeError:
        print('broken pipe')
        fedor.start_socket_shit()
        watch_on_target(fedor)


def watch_on_box(fedor):
    print('watch on box sequence')
    try:
        fedor.rotate_head(-10, 15, 0, absolute=True)
    except BrokenPipeError:
        print('broken pipe')
        fedor.start_socket_shit()
        watch_on_box(fedor)


def test(fedor):
    print('watch on box sequence')
    try:
        fedor.rotate_shoulder_L(0, 0, 90, absolute=True)
        fedor.rotate_shoulder_L(0, -15, 90, absolute=True)
        fedor.rotate_shoulder_L(0, -15, 30, absolute=True)
        # fedor.rotate_shoulder_L(0, -15, 0, absolute=True)
    except BrokenPipeError:
        print('broken pipe')
        fedor.start_socket_shit()
        test(fedor)


# 440 - 490: middle
# 435 - 450: middle
# 430 - 

# 490 -550
# near 429 462.72185430463577 494
# midd 463 479.8588957055215 496
# long 490 493.54716981132077 497
