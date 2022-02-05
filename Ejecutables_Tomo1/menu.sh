    #!/bin/bash
    #Control de flujo: case
    echo "---------ESCUELA POLITECNICA NACIONAL--------"
    echo "-----Operación de plataforma TurtleBot3 -----"
    echo "-Gabriela Romero"
    echo "-Rodrigo Ayala"
    echo "─── ⍙_⍙ ─────  "   
    echo "───(ᵔ▿ᵔ)───── 		"
    echo "───/)⏥ )─────  		"
    echo "────ง─ง ─────                  "
    echo "Bienvenid@s, por favor seleccione el modelo  "
    echo "del robot TurtleBot3 o si deseas ejecuar la"
    echo "conducción autónoma del robot           "
    echo "                                         "

PS3="Seleccionar el modelo robot: " 
select opt in Burger Waffle_Pi Autonomo Salir; 
do 
    case $opt in 
        Burger) 
            echo "Seleccionaste el modelo Burger"
            . burger_m.sh
            ;; 
        Waffle_Pi) 
            echo "Seleccionaste el modelo Waffle"
            . waffle_m.sh
            ;;             
        Autonomo) 
            echo "Modo de operación: Conducción autónoma"
            . autonomo.sh 
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
