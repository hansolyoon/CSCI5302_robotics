#!/usr/bin/env python
import rospy
import maestro
import time
from std_msgs.msg import Float64
from std_msgs.msg import Bool
from sensor_msgs.msg import Imu
from collections import deque

# initilize pololu control
servo = maestro.Controller()
# define center and range for Servo
CENTER_VALUE = 6500
EXTREME_LEFT = 4100
EXTREME_RIGHT = 7900
# initilize publisher
pub1 = rospy.Publisher('state', Float64, queue_size=10)
pub2 = rospy.Publisher('pid_enable', Bool, queue_size=10)
pub3 = rospy.Publisher('setpoint', Float64, queue_size=10)
pub4 = rospy.Publisher('setheading', Float64, queue_size=10)
# define global values
global control_effort_IR
control_effort_IR = 0
global control_effort_heading
control_effort_heading = 0
global controlEffort_IMU
controlEffort_IMU = 0
global setPoint
setPoint = 1800
global heading
heading = 260
global stateNumber
stateNumber = 1
global speed
speed = 8000
global bearing
bearing = 0
global flag
flag = False
global IMU_Coeff
IMU_Coeff = 500
global stopTime
stopTime = 2.5

# setup function
def setup():
    # servo
    servo.setSpeed(0, 0)
    servo.setAccel(0, 0)
    servo.setRange(0, EXTREME_LEFT, EXTREME_RIGHT)
    servo.setTarget(0, CENTER_VALUE)
    # motor
    servo.setSpeed(1, 0)
    servo.setAccel(1, 200)
    servo.setRange(1, 4000, 8000)
    servo.setTarget(0, 6000)
    # initilize node
    rospy.init_node('stateControl_node', anonymous = True)
    # subscribers
    rospy.Subscriber("control_effort_ir", Float64, callback1)
    rospy.Subscriber("control_effort_heading", Float64, callback2)
    rospy.Subscriber("bearing", Float64, callback3)
    rospy.Subscriber("imu/data", Imu, callback4)

def callback1(data):
    global control_effort_IR
    control_effort_IR = int(data.data)

def callback2(data):
    global control_effort_heading
    control_effort_heading = int(data.data)

def callback3(data):
    global bearing
    bearing = int(data.data)

def callback4(data):
    #print data.angular_velocity.z
    global controlEffort_IMU
    controlEffort_IMU = -int(data.angular_velocity.z*IMU_Coeff)

def worker():
    global stateNumber, speed, control_effort_IR, control_effort_heading, bearing, flag, IMU_Coeff, controlEffort_IMU, stopTime
    queue = deque([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    stateChangeTime = time.time()
    rate = rospy.Rate(200)
    while not rospy.is_shutdown():
        print "State: " + str(stateNumber)
        print "IR: Effort: " + str(control_effort_IR)
        print "Current heading: " + str(bearing)
        print "Heading Effort: " + str(control_effort_heading)
        # get IR readings
        front = servo.getPosition(6)
        if front == 0:
            ir_output_front = 3600
        else:
            ir_output_front = int(1.0/front*10e5)
        right = servo.getPosition(11)
        if right == 0:
            ir_output_right = 2200
        else:
            ir_output_right = int(1.0/right*10e5)
        print "IR Front: " + str(ir_output_front)
        print "IR Right: " + str(ir_output_right)
        queue.append(ir_output_front)

        for x in queue:
            if x > 3400:
                flag = False
        queue.popleft()
        if ir_output_right > 2800 and ir_output_right < 4000 and flag and stateNumber < 3:
            print "####################State Change#############################"
            servo.setTarget(0, 7000)
            rospy.Rate(300).sleep()
            servo.setTarget(1,3800)
            rospy.Rate(2.5).sleep()
            servo.setTarget(1,6000)
            rospy.Rate(200).sleep()
            stateNumber = stateNumber + 1
            stateChangeTime = time.time()
            flag = False
        if time.time() - stateChangeTime > 5:
            flag = True
        if stateNumber == 1:
            heading = 260
            speed = 6550
            setPoint = 2150
            stopTime = 5
        if stateNumber == 2:
            heading = 202
            speed = 6600
            setPoint = 2000
            stopTime = 4
        if stateNumber == 3:
            heading = 155;
            speed = 6550
            setPoint = 2300
        if stateNumber == 4:
            rospy.signal_shutdown("Incorrect State Number")
            break
        pub1.publish(ir_output_right)
        pub2.publish(True)
        pub3.publish(setPoint)
        pub4.publish(heading)
        servo.setTarget(0, int(CENTER_VALUE-control_effort_IR*0.7-control_effort_heading+controlEffort_IMU))
        servo.setTarget(1, int(speed - abs(control_effort_heading)*0.1))
        rate.sleep()
    if rospy.is_shutdown():
        servo.setTarget(0, CENTER_VALUE)
        servo.setTarget(1, 3000)

if __name__ == '__main__':
    try:
        setup()
        worker()
    except rospy.ROSInterruptException:
        pass
