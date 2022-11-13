from visual import *
import ctypes as ct
import numpy as np

'''
en esta actividad se nos solicito recrear los movimientos realizados por el sensor WIT, sabiendo las tramas que han
sido enviadas, almacenadonlas en un archivo de tipo bin.
Por lo que lo que haremos sera recrear las tramas a traves del archivo inercial.bin, y luego sabiendo las tramas
realizaremos los movimientos, para esto utilizaremos Vpython.
'''

class eTrama(ct.Structure):
    _fields_ = [
        ('B0', ct.c_ubyte),('B1', ct.c_ubyte),('B2', ct.c_ubyte),
        ('B3', ct.c_ubyte),('B4', ct.c_ubyte),('B5', ct.c_ubyte),
        ('B6', ct.c_ubyte),('B7', ct.c_ubyte),('B8', ct.c_ubyte),
        ('B9', ct.c_ubyte),('BA', ct.c_ubyte)
        ]

msg = open('inercial.bin','rb') #abrimos el archivo en modo de lectura binaria
datos = [] #escribimos cada uno de los bytes del archivo inercial.bin en un arreglo

for data in msg.read():
    datos.append(ord(data)) #guardamos el ordinal para obtener el valor en formato numerico

#codigo proporcionado por la actividad que nos define el objeto a mover y como fueron realizadas las rotaciones
#el cual fue editado para la reconstruccion de los movimientos

#las variables nOld, tienen el objetivo de servir como variables globales, almacenando el valor anterior del giro realizado
nOld_R = nOld_P =nOld_Y =0;

#creacion del entorno
WinM = display(title='Kinect',x=50, y=0,width=1000,height=1000,center=(0,0,0))
Base = box(pos=(0,-150,0),size=(500,3,500), color=color.blue)

'''
Objeto definido por la actividad al cual se le deberan aplicar los movimientos, el cual esta conformado por una
caja roja con dos lineas indicando el eje x e y.
'''
def Get_Frame(tFXYZ,nClr):
    oFr_B= frame(pos=tFXYZ)
    oFr_B.oB1=box(frame=oFr_B,pos=(0,0,0), size=(100,60,160), color=nClr)
    oFr_B.oB2=box(frame=oFr_B,pos=(0,0,0), size=(200,2,2), color=color.blue)
    oFr_B.oB3=box(frame=oFr_B,pos=(0,0,0), size=(2,200,2), color=color.green)
    return oFr_B

'''
la funcion Rota tiene el objetivo de rotar al objeto en funcion de de la nueva posicion del angulo en los ejes x,y,z
para esto lo que hacemos sera calcular la diferencia entre el angulo actual con el anterior y rotar dicho valor 
para cada uno de los ejes
'''
def Rota (xObj,Ax,Ay,Az):
    global nOld_R, nOld_P, nOld_Y #se define como global para que siempre sea el valor anterior
    #Eje X
    Dx = Ax - nOld_R
    xObj.rotate(angle = -1*math.radians(Dx),axis=(0,0,1),origin =(0,0,0))
    nOld_R = Ax  #Guardamos el nuevo Roll

    #Eje Z
    Dz = Az - nOld_Y
    xObj.rotate(angle = 1*math.radians(Dz),axis=(0,1,0), origin =(0,0,0))
    nOld_Y = Az #Guardamos el nuevo YAW

    #Eje Y
    Dy = Ay - nOld_P
    xObj.rotate (angle = -1*math.radians (Dy),axis=(1,0,0),origin =(0,0,0))
    nOld_P = Ay #Guardamos el nuevo Pitch

    return

aObj = [Get_Frame((0,0,0) ,color.red)] #creamos el objeto
'''
Ahora iteraremos por cada existente dentro del archivo inercial.bin, como las tramas estan compuestas por 11 bytes
nuestro i ira aumentando de 11 en 11.
Lo que haremos ahora sera recrear cada una de las tramas, como hemos detectado que se nos envia la inclinaciones del objeto,
Calcularemos el angulo en cada uno de los instantes, y con ayuda de la funcion Rota, rotaremos la distancia faltante
'''
i=0
while (true):
    while (i < len(datos)):
        Tr = datos[i:i+11] #reconstruimos la trama
        if(np.sum(Tr[:10])%256==Tr[10]): #comprobacion del checksum
            if (Tr[0] == 0x55): #verificamos la cabecera
                if (Tr[1] == 0x53): #verificamos que se nos indique la inclinacion

                    Ax = ((Tr[3] << 8 | Tr[2])/32768.0) * 180 #calculamos el Roll
                    Ay = ((Tr[5] << 8 | Tr[4])/32768.0) * 180 #calculamos el Pitch
                    Az = ((Tr[7] << 8 | Tr[6])/32768.0) * 180 #calculamos el Yaw
                    Te = ((Tr[9] << 8 | Tr[8])/340.0 ) + 36.53 #calculamos la Temperatura
                    Az = 0
                    Rota(aObj[0],Ax,Ay,Az) #llamamos a Rota
                    rate(10) #establecemos que este ciclo se ejecute un maximo de 10 veces por segundo
        i+=11 #aumentamos de 11 en 11, debido a que las tramas son de 11 bytes
    i=0