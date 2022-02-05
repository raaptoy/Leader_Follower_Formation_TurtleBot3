#!/bin/bash
gnome-terminal --tab --title="Main" --command="bash waffle.sh 'cd /etc; ls; $SHELL'"
gnome-terminal --tab --title="Menu1" --command="bash menu1.sh 'cd /etc; ls; $SHELL'"
cd /home/rodrigo/Escritorio/Ejecutables
