#!/usr/bin/env python
import rospy
import maestro
import time
from std_msgs.msg import Float64
from std_msgs.msg import Bool

servo = maestro.Controller()
CENTER_VALUE = 1500 * 4
EXTREME_LEFT = 1050 * 4
EXTREME_RIGHT = 1950 * 4

pub = rospy.Publisher('state', Float64, queue_size=10)
pub2 = rospy.Publisher('pid_enable', Bool, queue_size=10)

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
    rospy.init_node('pololuControl_node', anonymous = True)
    rospy.Subscriber("control_effort", Float64, callback)

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " Data to servo %f", data.data)
    servo.setTarget(0, CENTER_VALUE+int((data.data)))
    print "Servo: " + str(CENTER_VALUE-int((data.data)))
    #time.sleep(1)

def worker():
    rate = rospy.Rate(200)
    while not rospy.is_shutdown():
        pub2.publish(True)
        ir_output = int((servo.getPosition(6)/4+245)*16-17)
        print "IR: " + str(ir_output)
        if abs(5648 - ir_output) > 100:
            pub.publish(ir_output)
        else:
            pub.publish(5648)
        rate.sleep()

if __name__ == '__main__':
    try:
        setup()
        worker()
    except rospy.ROSInterruptException:
        pass
