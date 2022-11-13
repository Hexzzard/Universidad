from PIL import Image, ImageOps
import pygame

def pregunta2():

    f6=Image.open('F6.png')
    
    #iniciamos pygame
    pygame.init() 
    #definimos un color
    white = (255, 255, 255)
    #cargamos la imagen 
    image = pygame.image.load(r'F6.png')   
    #obtenemos el ancho y alto
    y = image.get_height()
    x = image.get_width()
    #creamos la superficie de display o pantalla
    display_surface = pygame.display.set_mode((x,y ))
    #dejamos de fondo la imagne cargada
    pygame.display.set_caption('Image') 
    #valores posibles de una suma de rgb
    vals=[0,18,27,36,45,54,63,72,81,90,99,108,
    117,126,135,144,153,162,171,180,189,198,207,
    216,225,234,243,252,261,270,279,288,297,306,
    315,324,333,342,351,360,369,378,387,396,405,
    414,423,432,441,450,459,468,477,486,495,504,
    513,522,531,540,549,558,567,576,585,594,603,
    612,621,630,639,648,657,666,675,684,693,702,
    711,720,729,738,747,756,765]
    #valores posibles de temperatura
    temp=[17.10,17.27,17.36,17.45,17.54,17.63,17.72,17.81,17.90,17.99,18.08,
    18.17,18.26,18.35,18.44,18.53,18.62,18.71,18.80,18.89,18.98,19.07,
    19.16,19.25,19.34,19.43,19.52,19.61,19.70,19.79,19.88,19.97,20.06,
    20.15,20.24,20.33,20.42,20.51,20.64,20.78,20.87,20.96,21.05,
    21.14,21.23,21.32,21.41,21.50,21.59,21.68,21.77,21.86,21.95,22.04,
    22.13,22.22,22.31,22.45,22.58,22.67,22.76,22.85,22.94,23.03,
    23.12,23.21,23.30,23.39,23.48,23.57,23.66,23.75,23.84,23.93,24.12,
    24.23,24.34,24.43,24.58,24.77,24.86,25.28,25.45,25.62,25.89]
    #ciclo para inciar la pantalla y los eventos
    while True : 
        #definimos el color de fondo y la imagen de fondo
        display_surface.fill(white) 
        display_surface.blit(image,(0, 0))
        #inciamos los eventos de pygame 
        for event in pygame.event.get() : 
            #definimos el exit de pygame
            if event.type == pygame.QUIT : 
                pygame.quit() 
                quit() 
            #definimos el evenmto de click del mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #obtenemos las coordenadas de la posicion x e y
                ex, ye = event.pos
                #cargamos la imagen con PIL
                im = f6.convert("RGB")
                #variable de pixeles
                pix = im.load()
                #variable para sumar los valores rgb
                total=sum(pix[ex,ye])
                #contador
                c=1
                #extraemos los valores de R, G, B
                valus=(pix[ex,ye])
                rr=valus[0]
                gg=valus[1]
                bb=valus[2]
                #ciclo para colorear los pixeles de la imagen
                a=True
                while a==True:
                    #definimos un rango de los valores
                    if total<=vals[c] and total>vals[c-1]:
                        #mostramos las posiciones x e y junto con la temperatura
                        print("click en: ","X:", ex,"Y:",ye,"  con temperatura:",temp[c],"°C")
                        #convertimos la imagen a rgb
                        ic = f6.convert("RGB")
                        #obtenemos los datos
                        d = ic.getdata()
                        #arreglo que contiene los valores de los canales
                        new_image = []
                        for item in d:
                            #definimos los rangos de valores para cada canal
                            if item[0] in list((range(rr-80, rr))) and item[1] in list((range(gg-80, gg))) and item[2] in list((range(bb-80, bb))):
                               #coloreamos con el nuevo valor rgb
                                new_image.append((0,255,0))
                            else:
                                new_image.append(item)         
                        # actualizamos los datos
                        ic.putdata(new_image)
                        #mostramos por pantalla
                        ic.show()
                        a=False
                    else:c+=1

            pygame.display.update()
pregunta2()
