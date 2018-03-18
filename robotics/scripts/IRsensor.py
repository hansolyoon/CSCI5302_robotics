import rospy
import Maestro
from std_msgs.msg import Float64

servo = maestro.Controller()

while 1:
    pub = rospy.Publisher('state', Float64, queue_size=10)
    rospy.init_node('statePubliser', anonymous=True)
    ir_output = servo.getPosition(6)
    pub.publish(ir_output)

servo.close
