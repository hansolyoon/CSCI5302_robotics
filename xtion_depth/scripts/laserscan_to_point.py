#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float64

class laserscanToPoint(object):

    def __init__(self):
        rospy.init_node('laserscan_to_point')
        rospy.Subscriber("/scan", LaserScan, self.conv_callback)
        self.pub = rospy.Publisher("/xtion_depth", Float64, queue_size=10)
        rospy.spin()

    def conv_callback(self, data):
        mid = data.ranges[len(data.ranges)/2]
        if mid > 0:
            self.pub.publish(mid)


if __name__ == '__main__':
    obj = laserscanToPoint()
