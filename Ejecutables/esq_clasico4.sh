#!/bin/sh
roscd
source ./devel/setup.bash
export TURTLEBOT3_MODEL=burger
#Lanzo Robots Diamante 
roslaunch multi_robot followers4.launch
#Lanzo el control del robot 1 (Teleoperación)
gnome-terminal --tab --title="Control Lider" --command="rosrun multi_robot lidermovimiento 'cd /etc; ls; $SHELL'"
#Follower2
gnome-terminal --tab --title="Seguidor 2" --command="rosrun multi_robot f2esq_clasico 'cd /etc; ls; $SHELL'"
#Follower3
gnome-terminal --tab --title="Seguidor 3" --command="rosrun multi_robot f3esq_clasico 'cd /etc; ls; $SHELL'"
#Follower4
gnome-terminal --tab --title="Seguidor 4" --command="rosrun multi_robot f4esq_clasico 'cd /etc; ls; $SHELL'"
cd /home/rodrigo/Escritorio/Ejecutables

