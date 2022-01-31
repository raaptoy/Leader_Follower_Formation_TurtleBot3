    #!/bin/bash
    #Control de flujo: case
    echo "---------ESCUELA POLITECNICA NACIONAL--------"
    echo "-----Control de Formación Líder-Seguidor -----"
    echo "-Gabriela Romero"
    echo "-Rodrigo Ayala"
    echo "─── ⍙_⍙ ─────  "   
    echo "───(ᵔ▿ᵔ)───── 		"
    echo "───/)⏥ )─────  		"
    echo "────ง─ง ─────                  "
    echo "Bienvenid@s, por favor seleccione el manejo  "
    echo "del robot líder"
    echo "                                             "

PS3="Seleccionar manejo del robot: " 
select opt in Teclado ROS_Mobile Salir; 
do 
    case $opt in 
        Teclado) 
            echo "Modo de operación: teclado"
            . teclado.sh
            ;; 
        ROS_Mobile) 
            echo "Modo de operación: Celular"
            . Ros_mobile.sh
            ;;                       
        Salir)
            break
            echo "Finalizó el programa con éxito"
            ;; 
        *) 
            echo "$REPLY no es una opción válida" 
            ;; 
    esac 
done
