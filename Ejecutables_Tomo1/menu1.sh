#!/bin/bash
    #Control de flujo: case
    echo "Escoje la forma en la que deseas"
    echo "operar la trayectoria del robot "
    echo "TurtleBot3 seleccionado        "
    echo "                                "
    echo "En el caso de escoger ROS Mobile"
    echo "seguir el proceso de configuración"
    echo "del trabajo escrito              "
    echo "                                "
    echo "                                "
   
PS3="Seleccionar el tipo de control: " 
select opt in Teclado ROS_Mobile salir; 
do 
    case $opt in 
        Teclado) 
            echo "Inicio la ejecución"
            . rosrun control_lider control_lider 
            ;;
        ROS_Mobile) 
            echo "Conecte la aplicación móvil"
            ;;              
        salir) 
            break
            ;; 
        *) 
            echo "$REPLY no es una opción válida" 
            ;; 
    esac 
done
