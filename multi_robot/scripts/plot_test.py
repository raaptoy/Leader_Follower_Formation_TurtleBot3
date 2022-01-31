#! /usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

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

#----------------------------CARGO LOS DATOS DESDE EL ARCHIVO DE TEXTO-----------------------
lider_pose_x = np.genfromtxt(LOG_FILE_DIR+'/lider_pose_x.csv', delimiter = ' , ')
lider_pose_y = np.genfromtxt(LOG_FILE_DIR+'/lider_pose_y.csv', delimiter = ' , ')

seguidorR2_pose_x = np.genfromtxt(LOG_FILE_DIR+'/seguidorR2_pose_x.csv', delimiter = ' , ')
seguidorR2_pose_y = np.genfromtxt(LOG_FILE_DIR+'/seguidorR2_pose_y.csv', delimiter = ' , ')
seguidorR2_pose_yaw = np.genfromtxt(LOG_FILE_DIR+'/seguidorR2_pose_yaw.csv', delimiter = ' , ')

seguidorR3_pose_x = np.genfromtxt(LOG_FILE_DIR+'/seguidorR3_pose_x.csv', delimiter = ' , ')
seguidorR3_pose_y = np.genfromtxt(LOG_FILE_DIR+'/seguidorR3_pose_y.csv', delimiter = ' , ')

seguidorR4_pose_x = np.genfromtxt(LOG_FILE_DIR+'/seguidorR4_pose_x.csv', delimiter = ' , ')
seguidorR4_pose_y = np.genfromtxt(LOG_FILE_DIR+'/seguidorR4_pose_y.csv', delimiter = ' , ')

# virtual_pose_x = np.genfromtxt(LOG_FILE_DIR+'/virtual_pose_x.csv', delimiter = ' , ')
# virtual_pose_y = np.genfromtxt(LOG_FILE_DIR+'/virtual_pose_y.csv', delimiter = ' , ')

# -------------------IGUALO EL TAMAÑO DE LOS VECOTRES QUE VOY A GRAFICAR-----------------------
lider_pose_x, lider_pose_y = igualar_vec(lider_pose_x, lider_pose_y)
seguidorR2_pose_x, seguidorR2_pose_y = igualar_vec(seguidorR2_pose_x, seguidorR2_pose_y)
seguidorR3_pose_x, seguidorR3_pose_y = igualar_vec(seguidorR3_pose_x, seguidorR3_pose_y)
seguidorR4_pose_x, seguidorR4_pose_y = igualar_vec(seguidorR4_pose_x, seguidorR4_pose_y)
#virtual_pose_x, virtual_pose_y = igualar_vec(virtual_pose_x, virtual_pose_y)


# --------------------------- GRAFICO LOS RESULTADOS -------------------------------------------- 
ax.plot(lider_pose_y, lider_pose_x, label='lider')
ax.plot(seguidorR2_pose_y, seguidorR2_pose_x, label = 'seguidor R2')
ax.plot(seguidorR3_pose_y, seguidorR3_pose_x, label = 'seguidor R3')
ax.plot(seguidorR4_pose_y, seguidorR4_pose_x, label = 'seguidor R4')
# ax.plot(virtual_pose_x, virtual_pose_y, label ='virtual')

#------------------------ CONFIGURACIÓN DE LOS EJES DEL GRÁFICO ------------------------------
ax.set_xlabel('Eje y')
ax.set_ylabel('Eje x')
ax.set_title('TRAYECTORIA DE LOS ROBOTS')
ax.legend()


#--------------------------INCLUYO LA ANIMACIÓN -------------------------------------------
c=np.size(lider_pose_x)
for i in range(c):
    if i % 3 ==0:
        plt.scatter(lider_pose_y[i], lider_pose_x[i], color='black')
        plt.scatter(seguidorR2_pose_y[i], seguidorR2_pose_x[i], color='blue')
        plt.scatter(seguidorR3_pose_y[i], seguidorR3_pose_x[i], color='red')
        plt.scatter(seguidorR4_pose_y[i], seguidorR4_pose_x[i], color='yellow')
        plt.pause(0.001)

plt.show()

