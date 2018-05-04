#!/usr/bin/env python
import maestro
import time

servo = maestro.Controller()
f = open("test3.txt","w")
while 1:
    ir_output_front = int(1.0/servo.getPosition(6)*10e5)
    ir_output_right = int(1.0/servo.getPosition(11)*10e5)
    f.write("Front: " + str(ir_output_front) + "\n")
    f.write("Right: " + str(ir_output_right) + "\n")
    time.sleep(0.001)

f.close()
