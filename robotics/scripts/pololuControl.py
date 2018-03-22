#!/usr/bin/env python
import rospy
import maestro
import time
from std_msgs.msg import Float64
from std_msgs.msg import Bool

# initilize the pololu control
servo = maestro.Controller()
# define center and range value for servo
CENTER_VALUE = 1500 * 4
EXTREME_LEFT = 4100
EXTREME_RIGHT = 7900
# initilize two publishers
pub = rospy.Publisher('state', Float64, queue_size=10)
pub2 = rospy.Publisher('pid_enable', Bool, queue_size=10)
# setup functio
def setup():
    servo.setSpeed(0, 0)
    servo.setAccel(0, 0)
    servo.setSpeed(1, 0)
    servo.setAccel(1, 0)
    servo.setRange(0, EXTREME_LEFT, EXTREME_RIGHT)
    servo.setTarget(0, CENTER_VALUE)
    servo.setRange(1, EXTREME_LEFT, EXTREME_RIGHT)
    time.sleep(1)

    # set servo speed
    servo.setTarget(1, 6200)
    #servo.setTarget(1, 6170)
    cmd_servo = CENTER_VALUE
    # initilize the ROS node
    rospy.init_node('pololuControl_node', anonymous = True)
    # initilize the Subscriber for PID output
    rospy.Subscriber("control_effort", Float64, callback)

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + " Data to servo %f", data.data)
    # operate the servo
    servo.setTarget(0, CENTER_VALUE-int((data.data)))
    #print "Servo: " + str(int((data.data)))
    #time.sleep(1)

def worker():
    # set frequnce
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        # make sure PID is enabled all the time
        pub2.publish(True)
        #ir_output = int((servo.getPosition(6)/4+245)*16-17)
        # inverse the measurement
        ir_output_left = int(1.0/servo.getPosition(6)*10e5)
        ir_output_right = int(1.0/servo.getPosition(7)*10e5)
        ir_output_diff = ir_output_left - ir_output_right
        print "IR: " + str(ir_output_diff)
        pub.publish(ir_output_diff)
        rate.sleep()
    if rospy.is_shutdown():
        servo.setTarget(1, 6000)

if __name__ == '__main__':
    try:
        setup()
        worker()
    except rospy.ROSInterruptException:
        pass
