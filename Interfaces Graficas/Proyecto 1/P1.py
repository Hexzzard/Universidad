from PIL import Image, ImageOps
import pygame
f1=Image.open('F1.png')
f2=Image.open('F2.png')
f3=Image.open('F3.png')
f4=Image.open('F4.png')
f5=Image.open('F5.png')
f6=Image.open('F6.png')
#Punto 1: adaptacion de la funcion mostrada
#para simplificar, esta funcion recibe una imagen y el nombre con que se guardara la imagen (para poder iterar dentro de un ciclo)7
#con esto calculara cada espacio de color y guardara cada uno como una imagen independiente
def separacion(img,name):
 im = img.copy()
 data = im.getdata()
 r = [(d[0], 0, 0) for d in data]
 g = [(0, d[1], 0) for d in data]
 b = [(0, 0, d[2]) for d in data]
 im.putdata(r)
 im.save(name+' R.png')
 im.putdata(g)
 im.save(name+' G.png')
 im.putdata(b)
 im.save(name+' B.png')
imgs = [f1,f2,f3,f4,f5,f6]
name = ['F1','F2','F3','F4','F5','F6']
for i in range(6):
 separacion(imgs[i],name[i])
#Punto 2: convertir los pixeles verdes a amarillo en F1
#convertimos la imagen al espacio de colores RGB y obtenemos la informacion
P2 = f1.convert("RGB")
d = P2.getdata()
#dentro de un arreglo vacio guardaremos el nuevo valor de los pixeles y los que sean considerados verdes ahora seran de color
#amarillo (se considera verde a los pixeles con un valor mayor a 30 en el canal G), tambien se aplico un sombreado por efectos esteticos
new_image = []
for item in d:
    if item[1] in list(range(30, 256)):
        new_image.append((int(255*(item[1]/255)), int(255*(item[1]/255)), 0)) #(255, 255,0) = amarillo
    else:
        new_image.append(item)
#ahora convertimos este arreglo a una imagen y lo guardamos
P2.putdata(new_image)
P2.save("f1_altered.jpg")
#Punto 3: cambiar los pixeles verdes a naranjo en F3
#aplicamos la misma logica que el punto anterior
P3 = f3.convert("RGB")
d = P3.getdata()
#ahora la definicion de verde debe ser mas especifica bajo el contexto de la imagen, se les considera ahora a los pixeles
#que tengan un valor superior a 10 en el canal G, en el canal B no deben poseer un valor superior a 10 y un valor entre 10 y 40 en el
#canal G, con esto me refiero a que no se forme una tonalidad azul, y finalmente en el canal R debe ser mayor a 120
new_image = []
for item in d:
    if ((item[1] in list(range(10, 256))) and not (item[2] in list(range(10, 256))and item[1] in list(range(10, 40)))and not (item[0] in list(range(120, 256)))):
        new_image.append((int(255*(item[1]/255)), int(128*(item[1]/255)), 0)) #(255, 128,0) = naranja
    else:
        new_image.append(item)
#guardamos la imagen, tambien se le aplico un sombreado por efectos esteticos
P3.putdata(new_image)
P3.save("f3_altered.jpg")
#P4: convertir a azul todas las ramificaciones de color rojo en F2
#aplicamos los mismos conceptos de los puntos anteriores
P4 = f2.convert("RGB")
d = P4.getdata()
new_image = []
#en el arreglo guardaremos la imagen con los pixeles de color rojo cambiados a azul
#la definicion de rojo sera que tenga un valor superior a 1 en el canal R y inferior a 120 en el canal G
for item in d:
    if ((item[0] in list(range(1, 256))) and (item[1] in list(range(0, 120)))):
        new_image.append((0, item[1], int(255*(item[0]/255))))
    else:
        new_image.append(item)
#guardamos
P4.putdata(new_image)
P4.save("f2_altered.jpg")
#P5: aislar las flores de color rojo en F4
#utilizamos los mismos conceptos
P5 = f4.convert("RGB")
d = P5.getdata()
new_image = []
#ahora lo que haremos sera eliminar todos los pixeles que no sean considerados rojos
#para ser considerado rojo debe poseer un valor superior a 150 en el canal R
for item in d:
 #ahora lo que haremos sera guardar en el arreglo todos los pixeles que sean considerados de color rojo
 #la definicion de rojo es que tenga un valor superior a 1 en el canal R y inferior a 120 en el canal G,
 #sino cumple esta condicion el pixel se torna negro (0,0,0)
    if item[0] in list(range(120, 256)):
        new_image.append(item)
    else:
        new_image.append((0, 0, 0))
#guardamos la imagen
P5.putdata(new_image)
P5.save("f4_altered.jpg")
#P6: aislar la flor en F5
#utilizamos los mismos conceptos de los puntos anteriores
P6 = f5.convert("RGB")
d = P6.getdata()
new_image = []
#ahora guardaremos en el arreglo los pixeles que sean considerados rosados, superior a 120 en el canal R y superior a 203 en el canal B
for item in d:
    if item[0] in list(range(0, 120)) and item[1] in list(range(0, 256)) and item[2] in list(range(0, 203)):
        new_image.append((0, 0, 0))
    else:
        new_image.append(item)
#guardamos la imagen
P6.putdata(new_image)
P6.save("f5_altered.jpg")