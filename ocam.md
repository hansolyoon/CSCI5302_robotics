cd libuvc
mkdir build
cd build
cmake ..
make
sudo make install
cd ~/catkin_ws/src/libuvc_ros/
rm -rf build
rm makefile
cd ~/catkin_ws
catkin_make
lsusb(to check dev No. of camera)

//roslaunch libuvc_camera uvccam.launch
rostopic list(to see rostopic)
//rqt(using another terminal)
