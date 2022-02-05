#!/bin/bash
export TURTLEBOT3_MODEL=burger
#Lanzo el mundo 
gnome-terminal --tab --title="Mundo" --command="bash mundo.sh 'cd /etc; ls; $SHELL'"
sleep 5s
gnome-terminal --tab --title="Camera1" --command="bash camera1.sh 'cd /etc; ls; $SHELL'"
sleep 2s
gnome-terminal --tab --title="Camera2" --command="bash camera2.sh 'cd /etc; ls; $SHELL'"
sleep 2s
gnome-terminal --tab --title="Lane" --command="bash lane.sh 'cd /etc; ls; $SHELL'"
sleep 2s
gnome-terminal --tab --title="autorace" --command="bash auto.sh 'cd /etc; ls; $SHELL'"
cd /home/rodrigo/Escritorio/Ejecutables
