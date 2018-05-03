#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def talker():
    pub1 = rospy.Publisher('setpoint', Float64, queue_size=10)
    pub2 = rospy.Publisher('heading1', Float64, queue_size=10)
    pub3 = rospy.Publisher('heading2', Float64, queue_size=10)
    pub4 = rospy.Publisher('heading3', Float64, queue_size=10)
    rospy.init_node('setPoint_node', anonymous=True)
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        pub1.publish(2500)
        pub2.publish(-66)
        pub3.publish(-166)
        pub4.publish(72)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
