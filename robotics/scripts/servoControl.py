#!/usr/bin/env/python
import rospy
import maestro
import time

from std_msgs.msg import String
CENTER_VALUE = 1500
EXTREME_LEFT = 1050
EXTREME_RIGHT = 1950

def setup():
    servo = maestro.Controller()
    servo.setSpeed(0, 0)
    servo.setAccel(0, 0)
    servo.setRange(0, EXTREME_LEFT, EXTREME_RIGHT)
    servo.setRange(1, EXTREME_LEFT, EXTREME_RIGHT)
    cmd_servo = CENTER_VALUE


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Data to servo %s", data.data)
    servo.setTarget(0, int(data.data) * 4)
    #time.sleep(1)

def listener():
    rospy.init_node('servoControl_node', anonymous = True)
    rospy.Subscriber("controlEffort", String, callback)
    rospy.spin()

if __name__ == '__main__':
    setup()
    listener()
