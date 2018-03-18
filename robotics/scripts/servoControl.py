#!/usr/bin/env/python
import rospy
import maestro
import time

from std_msgs.msg import String
CENTER_VALUE = 1500
EXTREME_LEFT = 1000
EXTREME_RIGHT = 2000


def setup():
    servo = maestro.Controller()
    servo.setSpeed(0, 0)
    servo.setAccel(0,0)
    cmd_servo = CENTER_VALUE    


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Data to servo %s", data.data)
    servo.setTarget(0, int(data.data) * 4)
    #time.sleep(1)
    
def listener():
    rospy.init_node('controlEffortNode', anonymous = True)
    rospy.Subscriber("controlEffort", String, callback)
    rospy.spin()

if __name__ == '__main__':
    setup()
    listener()
