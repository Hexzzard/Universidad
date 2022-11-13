Device 12F675
Dim Nadc[4] As Byte
Dim n As Byte
Dim h As Byte
Dim l As Byte

ANSEL = %00011111
CMCON = %00000111
TRISIO = %00010111

Nadc[0] = %10000011
Nadc[1] = %10000111
Nadc[2] = %10001011
Nadc[3] = %10001111

n = 0

Slc:
    ADCON0 = Nadc[n]
Dts:
    If ADCON0.1 = 1 Then GoTo Dts  'hasta que no termine la conversion no pasa a la siguiente instruccion
    h = ADRESH                      
    l = ADRESL
 
    'la trama es Canal, ADRESH, ADRESL, \n
    'baudmode 396 => BaudRate=2400, 8-bit no-parity, non inverted
    SerOut GPIO.5,  396, [#n, ",", #h, ",", #l, 13,10,0]
    DelayMS 1000
    n = n + 1
    If n = 4 Then n = 0
    GoTo Slc
    End 
