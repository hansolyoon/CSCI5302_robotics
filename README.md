# CSCI5302_robotics

### history (for odroid)

1. Save directory <br>
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

4. setup for maestro.py <br>
  https://github.com/FRC4564/Maestro
  
5. run rc.py
```
$rosrun robotics rc.py
```

6. how to code? <br>
  https://www.pololu.com/docs/0J40/5.e (channel setting manual)<br>
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

---

### How to use

- Download rc.py<br>
- Modify it<br>
- Connect your wifi to "Adroidhotspot2184"(hansol's hotspot)<br>
- Upload your modified file to odroid
```
scp -r /<your folder>/rc.py odroid@192.168.43.11:/home/odroid/catkin_ws/src/robotics/scripts/rc.py
```
- connect to odroid
```
$ssh odroid@192.168.43.11
```
- run roscore
```
odroid@192.168.43.11$ roscore (leave this terminal and open one more terminal)
```
- follow step 2, 3, 5 mentioned above 'history'<br>
```
$cd catkin_ws
$rospack profile
$catkin_make
$rosrun robotics rc.py
```
