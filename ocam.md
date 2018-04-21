cd libuvc<br>
mkdir build<br>
cd build<br>
cmake ..<br>
make<br>
sudo make install<br>
cd ~/catkin_ws/src/libuvc_ros/<br>
rm -rf build<br>
rm makefile<br>
cd ~/catkin_ws<br>
catkin_make<br>
lsusb(to check dev No. of camera)<br>

//roslaunch libuvc_camera uvccam.launch<br>
rostopic list(to see rostopic)<br>
//rqt(using another terminal)
