#!/usr/bin/env python
import maestro

servo = maestro.Controller()
f = open("test.txt")
while 1:
    ir_output_front = int(1.0/servo.getPosition(6)*10e5)
    ir_output_right = int(1.0/servo.getPosition(11)*10e5)
    f.write("Front: " + ir_output_front)
    f.write("Right: " + ir_output_right)

f.close()
