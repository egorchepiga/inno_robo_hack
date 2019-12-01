import Robot as class_fedor
import time


fedor = class_fedor.Robot('10.127.50.62', 10099)


fedor.head.rotate(-30)

time.sleep(1)

fedor.hand.right.elbow.fold(-95)

time.sleep(1)

fedor.hand.right.wrist.rotate(-90)

time.sleep(1)

fedor.hand.right.elbow.rotation(-55)

time.sleep(1)

fedor.torso.tilt(55)

time.sleep(1)

fedor.hand.right.shoulder.move(-90)

time.sleep(1)

fedor.hand.right.shoulder.move(-90)

time.sleep(1)

fedor.hand.right.shoulder.move(-100)

time.sleep(1)

fedor.hand.right.wrist.rotate(-100)

time.sleep(1)

fedor.torso.rotate(15)

time.sleep(1)

fedor.hand.right.wrist.front(8)

time.sleep(1)

fedor.hand.right.palm.thumb.fold(-90)

time.sleep(1)

fedor.hand.right.palm.ring.fold(90)

time.sleep(1)

fedor.hand.right.palm.little.fold(90)

time.sleep(5)


fedor.hand.right.wrist.front(10)

time.sleep(1)

fedor.torso.tilt(-90)

time.sleep(1)

fedor.hand.right.shoulder.move(60)

fedor.hand.right.elbow.fold(900)

fedor.torso.rotate(-70)

fedor.hand.right.palm.ring.fold(-90)

fedor.hand.right.palm.little.fold(-90)
