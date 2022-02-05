#!/bin/bash 
cd /home/rodrigo/catkin_ws/src
source ./devel/setup.bash
roslaunch turtlebot3_autorace_camera extrinsic_camera_calibration.launch
