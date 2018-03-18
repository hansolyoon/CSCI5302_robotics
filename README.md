# CSCI5302_robotics

###history (for odroid)

1. Save directory
  : ~/catkin_ws/src/robotics

2. update&make package
```
$cd catkin_ws
$rospack profile
$catkin_make
```

3. make python script executable
```
$cd ~/catkin_ws/src/robotics/scripts
$chmod +x rc.py
$chmod +x maestro.py
```

4. setup for maestro.py
  https://github.com/FRC4564/Maestro
  
5. run rc.py
```
$rosrun robotics rc.py
```

6. how to code?
  https://www.pololu.com/docs/0J40/5.e (channel setting manual)
  https://www.pololu.com/docs/0J40/4.b (serial servo commands manual)

```
import maestro.py
servo = maestro.Controller()
servo.setAccel(0,4)      #set servo 0 acceleration to 4
servo.setTarget(0,6000)  #set servo 0 target to 1500 (when I put 6000, maestro will be 6000/4)
servo.close
```
- acc and speed are for changing to react time
- need to put *time.sleep(1)* to send same command again
