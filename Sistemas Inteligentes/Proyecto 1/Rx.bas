Device 12F675
Xtal = 4  'frecuencia de 4mhz
'apagamos watchdogg y usamos reloj interno
Reminders off
    Config MCLRE_OFF, WDT_OFF, INTRC_OSC_NOCLKOUT
Reminders On

Dim i[8] As Byte
All_Digital= true  'todos los pines digitales

TRISIO = %00000001

rx:
    'para el envio de informacion se utilizo el modificador Str, la cual carga una trama obtenida del rx (8 bytes/caracteres),
    'la cual es utilizada para el envio de string como bytes, esta convierte los bytes en un string para luego enviarlos por puerto serial
    'baudmode 396 => BaudRate=2400, 8-bit no-parity, non inverted
    SerIn GPIO.0, 396, [Str i]
    SerOut GPIO.4, 396, [Str i,10]
    SerOut GPIO.5, 396, [Str i,10]
GoTo rx
End  
