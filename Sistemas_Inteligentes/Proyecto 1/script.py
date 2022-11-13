import serial        #cargamos el modulo serial
#establecemos una conecion de 2400/8n1 por el puerto COM2
com_serial = serial.Serial('COM2', baudrate=2400, bytesize =8, parity = 'N', stopbits=1)

#dentro de un ciclo leemos lo contenido en el puerto COM2, la cual se decodifica y se eliminan los saltos de linea adicionales
#finalmente se muestra por pantalla lo obtenido
while (True):
    data = com_serial.readline()
    s = data.decode('utf-8')
    s = s.rstrip('\n')
    print(s)

