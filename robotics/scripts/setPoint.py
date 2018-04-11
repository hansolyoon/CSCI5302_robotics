#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def talker():
    pub = rospy.Publisher('setpoint', Float64, queue_size=10)
    rospy.init_node('setPoint_node', anonymous=True)
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        hello = 0
        #rospy.loginfo(hello)
        pub.publish(hello)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
