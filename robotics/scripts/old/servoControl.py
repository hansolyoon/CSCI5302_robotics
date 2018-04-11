#!/usr/bin/env python
import rospy
import maestro
import time

from std_msgs.msg import Float64
servo = maestro.Controller()
CENTER_VALUE = 1500 * 4
EXTREME_LEFT = 1050 * 4
EXTREME_RIGHT = 1950 * 4

def setup():
    servo.setSpeed(0, 0)
    servo.setAccel(0, 0)
    servo.setSpeed(1, 0)
    servo.setAccel(1, 4)
    servo.setRange(0, EXTREME_LEFT, EXTREME_RIGHT)
    servo.setTarget(0, CENTER_VALUE)
    servo.setRange(1, EXTREME_LEFT, EXTREME_RIGHT)
    servo.setTarget(1, 6000)
    time.sleep(1)
    servo.setTarget(1, 6150)

    cmd_servo = CENTER_VALUE


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Data to servo %f", data.data)
    servo.setTarget(0, CENTER_VALUE+int((data.data)))
    print "Servo: " + str(CENTER_VALUE-int((data.data)))
    #time.sleep(1)

def listener():
    setup()
    rospy.init_node('servoControl_node', anonymous = True)
    rospy.Subscriber("control_effort", Float64, callback)
    rospy.spin()

if __name__ == '__main__':
    setup()
    listener()
