#!/usr/bin/env python
import math
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import Imu
from sensor_msgs.msg import MagneticField
from geometry_msgs.msg import Vector3Stamped

global lastAngles
gravity = [0,0,9.8]
magField = [0,0,0]
lastAngles = [0,0,0]

pub = rospy.Publisher('bearing', Float64, queue_size=10)

def setup():
    rospy.init_node("bearing_node", anonymous = True)
    rospy.Subscriber("imu/data", Imu, callback1)
    rospy.Subscriber("imu/mag", Vector3Stamped, callback2)

def callback1(data):
    global gravity
    gravity = [data.linear_acceleration.x,data.linear_acceleration.y,data.linear_acceleration.z]
    #print gravity
def callback2(data):
    global magField
    magField = [data.vector.x,data.vector.y,data.vector.z]
    #print magField

def worker():
    rate = rospy.Rate(200)
    while not rospy.is_shutdown():
        rollAngle = math.atan2(gravity[1], gravity[2])
        pitchAngle = math.atan(-gravity[0]/(gravity[1]*math.sin(rollAngle)+gravity[2]*math.cos(rollAngle)))
        yawAngle = math.atan2(magField[2]*math.sin(rollAngle)-magField[1]*math.cos(rollAngle),
        magField[0]*math.cos(pitchAngle)+magField[1]*math.sin(pitchAngle)*math.sin(rollAngle)+magField[2]*math.sin(pitchAngle)*math.cos(rollAngle))
        bearingAngle = yawAngle * (180.0/math.pi)
        if not math.isnan(bearingAngle):
            #print bearingAngle
            pub.publish(bearingAngle)
        rate.sleep()

if __name__ == '__main__':
    try:
        setup()
        worker()
    except rospy.ROSInterruptException:
        pass
