#! /usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import math as m

LOG_FILE_DIR = '/home/rodrigo/catkin_ws/src/multi_robot/Data'


def igualar_vec(vector_x, vector_y):
    a= np.size(vector_x)
    b=np.size(vector_y)
    print("Tamaño del vector x",a)
    print("Tamaño del vector y",b)
    while a != b:
        if a>b:
            vector_x = np.delete(vector_x,a-1)
        if b>a:
            vector_y = np.delete(vector_y,b-1)
        a= np.size(vector_x)
        b=np.size(vector_y)

    print("Tamaño del vector Función x",a)
    print("Tamaño del vector Función y",b)
    
    return vector_x, vector_y


    
fig, ax = plt.subplots()
fig, ax2 = plt.subplots()
ld=0.5
phid=-m.pi/2
error_angulo=0
error_distancia=0

#----------------------------CARGO LOS DATOS DESDE EL ARCHIVO DE TEXTO-----------------------

seguidorR2_distancia = np.genfromtxt(LOG_FILE_DIR+'/seguidorR2_distancia.csv', delimiter = ' , ')
seguidorR2_angulo = np.genfromtxt(LOG_FILE_DIR+'/seguidorR2_angulo.csv', delimiter = ' , ')
seguidorR2_distanciad = np.genfromtxt(LOG_FILE_DIR+'/seguidorR2_distanciad.csv', delimiter = ' , ')
seguidorR2_angulod = np.genfromtxt(LOG_FILE_DIR+'/seguidorR2_angulod.csv', delimiter = ' , ')


# -------------------IGUALO EL TAMAÑO DE LOS VECOTRES QUE VOY A GRAFICAR-----------------------

seguidorR2_distancia, seguidorR2_distanciad = igualar_vec(seguidorR2_distancia, seguidorR2_distanciad)
seguidorR2_angulod, seguidorR2_angulo = igualar_vec(seguidorR2_angulod, seguidorR2_angulo)

seguidorR2d_eje_x = np.linspace(0, np.size(seguidorR2_distancia)-1, np.size(seguidorR2_distancia))
seguidorR2a_eje_x = np.linspace(0, np.size(seguidorR2_angulo)-1, np.size(seguidorR2_angulod))


# --------------------------- OBTENCIÓN DEL ISE  -------------------------------------------- 
for i in range(np.size(seguidorR2d_eje_x)):
    error_distancia += np.abs(seguidorR2_distancia[i]-seguidorR2_distanciad[i])
for i in range(np.size(seguidorR2a_eje_x)):
    error_angulo += np.abs(seguidorR2_angulo[i]- seguidorR2_angulod[i])



# --------------------------- GRAFICO LOS RESULTADOS -------------------------------------------- 

ax.plot(seguidorR2d_eje_x, seguidorR2_distanciad, label = 'Referencia', color='red', linestyle='solid', linewidth=1)
ax.plot(seguidorR2d_eje_x, seguidorR2_distancia, label = 'Seguidor R2', color='blue', linestyle='dashed', linewidth=2)

ax2.plot(seguidorR2a_eje_x, seguidorR2_angulod, label='Referencia', color='red', linestyle='solid', linewidth=1)
ax2.plot(seguidorR2a_eje_x, seguidorR2_angulo, label = 'Seguidor R2', color='blue', linestyle='dashed', linewidth=2)


print ("Error ángulo: ", error_angulo)
ise_angulo=error_angulo**(2)
print ("ISE ángulo: ", ise_angulo)

ise_distancia=error_distancia**(2)
print ("Error distancia: ", error_distancia)
print ("ISE distancia", ise_distancia)


#------------------------ CONFIGURACIÓN DE LOS EJES DEL GRÁFICO ------------------------------
ax.set_xlabel('Iteraciones')
ax.set_ylabel('Distancia [m]')
ax.set_title('Distancia Líder seguidor esquema clásico')
ax.legend()
ax.grid(color='k', linestyle='--', linewidth=0.4)

ax2.set_xlabel('Iteraciones')
ax2.set_ylabel('Ángulo [rad]')
ax2.set_title('Ángulo Líder seguidor esquema clásico')
ax2.legend()
ax2.grid(color='k', linestyle='--', linewidth=0.4)

plt.show()
