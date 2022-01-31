#!/bin/bash
gnome-terminal --tab --title="Main" --command="bash mundo.sh 'cd /etc; ls; $SHELL'"
sleep 10s
gnome-terminal --tab --title="Menu1" --command="bash esq_clasico_rm.sh 'cd /etc; ls; $SHELL'"

cd /home/rodrigo/Escritorio/Ejecutables
