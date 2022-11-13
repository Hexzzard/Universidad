from PIL import Image, ImageOps
import pygame

#funciones modificadas de la pregunta 1 para 3 o 4 cancales
#3 canales poseen el espacio RGB y HSV
#4 canales poseen el espacion RGBA y CMYK
#grey solo posee un canal, por lo que no se hace nada

#las funciones separan cada imagen por canal y lo guardan, usa un string para el nombre del archivo y otro para el formato
def RGB(img,name,formato):
    data = img.getdata()
    c1 = [(d[0], 0, 0) for d in data]
    c2 = [(0, d[1], 0) for d in data]
    c3 = [(0, 0, d[2]) for d in data]
    img.putdata(c1)
    img.save(name+formato[0])
    img.putdata(c2)
    img.save(name+formato[1])
    img.putdata(c3)
    img.save(name+formato[2])

def RGBA(img,name,formato):
    #para visualizar el contenido en la imagen se debe poner un 255 en el canal alfa
    #por lo que tecnicamente no es el contenido bruto del canal
    data = img.getdata()
    c1 = [(d[0], 0, 0, 255) for d in data]
    c2 = [(0, d[1], 0, 255) for d in data]
    c3 = [(0, 0, d[2], 255) for d in data]
    c4 = [(0, 0, 0, d[3]) for d in data]
    img.putdata(c1)
    img.save(name+formato[0])
    img.putdata(c2)
    img.save(name+formato[1])
    img.putdata(c3)
    img.save(name+formato[2])
    img.putdata(c4)
    img.save(name+formato[3])

def CMYK(img,name,formato):
    data = img.getdata()
    c1 = [(d[0], 0, 0, 0) for d in data]
    c2 = [(0, d[1], 0, 0) for d in data]
    c3 = [(0, 0, d[2], 0) for d in data]
    c4 = [(0, 0, 0, d[3]) for d in data]
    img.putdata(c1)
    img.save(name+formato[0])
    img.putdata(c2)
    img.save(name+formato[1])
    img.putdata(c3)
    img.save(name+formato[2])
    img.putdata(c4)
    img.save(name+formato[3])

def HSV(img,name,formato):
    #como no encontramos algun formato que soporte el espacio de colores HSV
    #despues de separar por canal convertimos a rgb para guardar la imagen
    data = img.getdata()
    c1 = [(d[0], 0, 0) for d in data]
    c2 = [(0, d[1], 0) for d in data]
    c3 = [(0, 0, d[2]) for d in data]
    hsv.putdata(c1)
    hsv.convert('RGB').save(name+formato[0])
    hsv.putdata(c2)
    hsv.convert('RGB').save(name+formato[1])
    hsv.putdata(c3)
    hsv.convert('RGB').save(name+formato[2])

name = ['F1.png','F2.png','F3.png','F4.png ','F5.png','F6.png']
sname = ['F1','F2','F3','F4 ','F5','F6']

#iteramos por cada imagen y llamamos a cada una de las anteriores funciones, separando cada imagen en los canales 
for i in range(6):
    #espacio en escala de grises
    gray =Image.open(name[i]).convert('L')
    gray.save(sname[i]+' gray.png')
    #RGB
    rgb= Image.open(name[i]).convert('RGB')
    RGB(rgb,sname[i],[' R.png',' G.png',' B.png'])
    #CMYK
    rgba= Image.open(name[i]).convert('RGBA')
    RGBA(rgba,sname[i],[' RR.png',' GG.png',' BB.png',' A.png'])
    #CMYK
    cmyk= Image.open(name[i]).convert('CMYK')
    CMYK(cmyk,sname[i],[' C.jpeg',' M.jpeg',' Y.jpeg',' K.jpeg'])
    #HSV
    hsv= Image.open(name[i]).convert('HSV')
    HSV(hsv,sname[i],[' H.png',' S.png',' V.png'])
