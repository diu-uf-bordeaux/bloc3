import serial

# Ouverture de la ligne série 115200 bauds
port = serial.Serial('/dev/ttyUSB0', 115200)

while True:
    print('Valeur à envoyer:')
    valeur = input().encode('utf-8')
    port.write(valeur + b"\n")