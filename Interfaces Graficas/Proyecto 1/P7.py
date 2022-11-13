from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import pygame

#definimos la funcion del histograma normal
#recibiendo el nombre del archivo como los datos del histograma
def graficaN(datos, nombre_del_archivo):
    #creamos una figura
    plt.figure(1)
    #variable del largo de los datos
    x=range(len(datos))
    #creacion de los valores 
    plt.xticks([0, 50, 100, 150, 200, 255],[0, 50, 100, 150, 200, 255])
    #alineamos los datos con el largo de este
    plt.bar(x, datos, align='center', color=(0,0,0))
    #añadimos un titulo
    plt.title('Histograma Normal')
    #guardamos la imagen en la figura
    plt.savefig(nombre_del_archivo, bbox_inches='tight')
    return None
#definimos la funcion del histograma acomulativo
#funcion para graficar y guardar la imagen del histograma
def graficaC(datos, nombre_del_archivo):
    #creamos una figura
    plt.figure(1)
    #variable del largo de los datos
    x=range(len(datos))
    #creacion de los valores 
    plt.xticks([0, 50, 100, 150, 200, 255],[0, 50, 100, 150, 200, 255])
    #alineamos los datos con el largo de este
    plt.bar(x, datos, align='center', color=(0,0,0))
    #añadimos un titulo
    plt.title('Histograma Acomulativo')
    #guardamos la imagen en la figura
    plt.savefig(nombre_del_archivo, bbox_inches='tight')
    return None
es=1
while es!=5:
    if es==1 or es==4:
        #abrimos la imagen convirtiendola en escala gris
        foto=Image.open('F'+str(es)+'.png').convert('CMYK')
        #obtenemos los datos del histograma
        histograma=foto.histogram()
        #arreglo para almacenar el histograma acomulativo
        h_acumulativo=[]
        #contador
        sumatoria=0
        #funcion del histograma acumulativo
        for valor in histograma:
            #aumenta el contador
            sumatoria+=valor
            #añadimos el valor anterior al arreglo
            h_acumulativo.append(sumatoria)
        graficaN(histograma, 'F'+str(es)+'_histogram-CMYK.png')
        graficaC(h_acumulativo, 'F'+str(es)+'_histogram-acumulative-CMYK.png')
    es+=1
