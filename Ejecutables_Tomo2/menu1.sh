#!/bin/bash
    #Control de flujo: case
    echo "Tipos de formación"
    echo "A continuación se muestra la "
    echo "formación para 3 y 4 agentes"
    echo "EC: Esquema Clásico          "
    echo "RV: Referencia Virtual          "
    echo "Esperar que se cargue Gazebo con"
    echo "el robot líder waffle pi"
    echo "1) Formación Fila"
    echo "   (3A)  * * *      "
    echo "   (4A)  * * * *     "
    echo "2) formación Columna"
    echo "        (3A) (4A) "
    echo "         *    *   "
    echo "         *    *   "
    echo "         *    *   "
    echo "              *   "
    echo "3) formación V"
    echo "(Válido solo para (3A) )"
    echo "     *   * "
    echo "       * "
    echo "4) formación Diamante"
    echo "(Válido solo para (4A) )"
    echo "       * "
    echo "     *   * "
    echo "       * "
PS3="Seleccionar el número de agentes: " 
select opt in 3Agentes_EC 4Agentes_EC 3Agentes_RV 4Agentes_RV salir; 
do 
    case $opt in 
        3Agentes_EC) 
            echo "Inicio la ejecución"
            . esq_clasico3.sh
            ;;
        4Agentes_EC) 
            echo "Inicio la ejecución"
            . esq_clasico4.sh
            ;;
        3Agentes_RV) 
            echo "Inicio la ejecución"
            . ref_virtual3.sh
            ;;
        4Agentes_RV) 
            echo "Inicio la ejecución"
            . ref_virtual4.sh
            ;;               
        salir) 
            break
            ;; 
        *) 
            echo "$REPLY no es una opción válida" 
            ;; 
    esac 
done
