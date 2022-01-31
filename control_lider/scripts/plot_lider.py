#! /usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

LOG_FILE_DIR = '/home/rodrigo/catkin_ws/src/control_lider/Data'


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

def orientacion(pose_x, pose_y, pose_yaw):
    #Punto inicial 
    y_ini,x_ini, yaw_ini=pose_y[1], pose_x[1], pose_yaw[1]
    ax.arrow(x_ini, y_ini, np.cos(yaw_ini)*0.2, np.sin(yaw_ini)*0.2, head_width=0.1,color='red' ,ec='black')
    
    #Punto Medio
    c=np.size(pose_x)
    d=int(c/2)
    y_med,x_med, yaw_med=pose_y[d], pose_x[d], pose_yaw[d]
    #print(yaw_med)
    ax.arrow(x_med, y_med, np.cos(yaw_med)*0.2, np.sin(yaw_med)*0.2, head_width=0.1,color='red' ,ec='black')

     #Punto cuarto
    e=int(c/4)
    y_med,x_med, yaw_med=pose_y[e], pose_x[e], pose_yaw[e]
    #print(yaw_med)
    ax.arrow(x_med, y_med, np.cos(yaw_med)*0.2, np.sin(yaw_med)*0.2, head_width=0.1,color='red' ,ec='black')

    #Punto tres/cuartos
    f=int(c*3/4)
    y_med,x_med, yaw_med=pose_y[f], pose_x[f], pose_yaw[f]
    #print(yaw_med)
    ax.arrow(x_med, y_med, np.cos(yaw_med)*0.2, np.sin(yaw_med)*0.2, head_width=0.1,color='red' ,ec='black')
    
    
    #Punto Final 
    y_fin,x_fin, yaw_fin=pose_y[c-1], pose_x[c-1], pose_yaw[c-1]
    #print(yaw_fin)
    ax.arrow(x_fin, y_fin, np.cos(yaw_fin)*0.2, np.sin(yaw_fin)*0.2, head_width=0.1,color='red' ,ec='black')

    return
    
def orientacion1(pose_x, pose_y, pose_yaw):
    #Punto inicial 
    y_ini,x_ini, yaw_ini=pose_y[1], pose_x[1], pose_yaw[1]
    ax.arrow(x_ini, y_ini, np.cos(yaw_ini)*0.2, np.sin(yaw_ini)*0.2, head_width=0.1,color='blue' ,ec='black')
    
    #Punto Medio
    c=np.size(pose_x)
    d=int(c/2)
    y_med,x_med, yaw_med=pose_y[d], pose_x[d], pose_yaw[d]
    #print(yaw_med)
    ax.arrow(x_med, y_med, np.cos(yaw_med)*0.2, np.sin(yaw_med)*0.2, head_width=0.1, color='blue' ,ec='black')

     #Punto cuarto
    e=int(c/4)
    y_med,x_med, yaw_med=pose_y[e], pose_x[e], pose_yaw[e]
    #print(yaw_med)
    ax.arrow(x_med, y_med, np.cos(yaw_med)*0.2, np.sin(yaw_med)*0.2, head_width=0.1, color='blue' ,ec='black')

    #Punto tres/cuartos
    f=int(c*3/4)
    y_med,x_med, yaw_med=pose_y[f], pose_x[f], pose_yaw[f]
    #print(yaw_med)
    ax.arrow(x_med, y_med, np.cos(yaw_med)*0.2, np.sin(yaw_med)*0.2, head_width=0.1,color='blue' ,ec='black')
    
    
    #Punto Final 
    y_fin,x_fin, yaw_fin=pose_y[c-1], pose_x[c-1], pose_yaw[c-1]
    #print(yaw_fin)
    ax.arrow(x_fin, y_fin, np.cos(yaw_fin)*0.2, np.sin(yaw_fin)*0.2, head_width=0.1, color='blue' ,ec='black')

    return

fig, ax = plt.subplots()

#----------------------------CARGO LOS DATOS DESDE EL ARCHIVO DE TEXTO-----------------------
lider_pose_x = np.genfromtxt(LOG_FILE_DIR+'/lider_pose_x_refa.csv', delimiter = ' , ')
lider_pose_y = np.genfromtxt(LOG_FILE_DIR+'/lider_pose_y_refa.csv', delimiter = ' , ')
lider_pose_yaw = np.genfromtxt(LOG_FILE_DIR+'/lider_pose_yaw_refa.csv', delimiter = ' , ')

lider_pose_x_tleop = np.genfromtxt(LOG_FILE_DIR+'/lider_pose_x_mw.csv', delimiter = ' , ')
lider_pose_y_tleop = np.genfromtxt(LOG_FILE_DIR+'/lider_pose_y_mw.csv', delimiter = ' , ')
lider_pose_yaw_tleop = np.genfromtxt(LOG_FILE_DIR+'/lider_pose_yaw_mw.csv', delimiter = ' , ')





# -------------------IGUALO EL TAMAÑO DE LOS VECOTRES QUE VOY A GRAFICAR-----------------------
lider_pose_x, lider_pose_yaw = igualar_vec(lider_pose_x, lider_pose_yaw)
lider_pose_x, lider_pose_y = igualar_vec(lider_pose_x, lider_pose_y)


lider_pose_x_tleop, lider_pose_yaw_tleop = igualar_vec(lider_pose_x_tleop, lider_pose_yaw_tleop)
lider_pose_x_tleop, lider_pose_y_tleop = igualar_vec(lider_pose_x_tleop, lider_pose_y_tleop)



# --------------------------- GRAFICO LOS RESULTADOS -------------------------------------------- 

ax.plot(lider_pose_x, lider_pose_y, label='Conducción Autónoma', color='red', linestyle='solid', linewidth=2)
ax.plot(lider_pose_x_tleop, lider_pose_y_tleop, label='Conducción Usuario Teclado', color='blue', linestyle='dashed', linewidth=2)


# ax.plot(seguidorR4_pose_x, seguidorR4_pose_y, label = 'seguidor R4', color='purple', linestyle='solid', linewidth=2)

#------------------PUNTOS ORIENTACIÓN-----------------------------

orientacion(lider_pose_x, lider_pose_y, lider_pose_yaw)
orientacion1(lider_pose_x_tleop, lider_pose_y_tleop, lider_pose_yaw_tleop)

# orientacion(seguidorR4_pose_x, seguidorR4_pose_y, seguidorR4_pose_yaw)



#------------------------ CONFIGURACIÓN DE LOS EJES DEL GRÁFICO ------------------------------
ax.set_xlabel('Posición x [m]')
ax.set_ylabel('Posición y [m]')
ax.set_title('Trayectoria TurtleBot3 Waffle Pi')
ax.legend()
ax.grid(color='k', linestyle='--', linewidth=0.4)

plt.show()

