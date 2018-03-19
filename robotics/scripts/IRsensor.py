#!/usr/bin/env python
import rospy
import maestro
import time
from std_msgs.msg import Float64

servo = maestro.Controller()

while not rospy.is_shutdown():
    pub = rospy.Publisher('state', Float64, queue_size=10)
    rospy.init_node('getDistance_node', anonymous=True)
    ir_output = int((servo.getPosition(6)/4+245)*16-17)
    if abs(5648 - ir_output) > 100
        pub.publish(ir_output)
    else:
        pub.publish(5648)
    time.sleep(1/50)

servo.close
