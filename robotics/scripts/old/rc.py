#! /usr/bin/env python
import rospy
import maestro
import time

servo = maestro.Controller()

# servo.setRange(0, 1200, 1650)
# servo.setRange(1, 1400, 1600)

servo.setSpeed(0, 0)
servo.setAccel(0, 0)

cmd_servo = 1500
servo.setTarget(0,cmd_servo*4)
time.sleep(1)

cmd_servo = 1000
servo.setTarget(0,cmd_servo*4)
time.sleep(1)

cmd_servo = 1500
servo.setTarget(0,cmd_servo*4)

cnt=1
while 1:
    cnt = cnt + 1
    ir_output = servo.getPosition(6)
    print "<<%d>>:%d" % (cnt, ir_output/4)

servo.close
