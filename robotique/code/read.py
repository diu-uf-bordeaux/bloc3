import serial
import numpy as np

# Ouverture de la ligne série 115200 bauds
port = serial.Serial('/dev/ttyUSB0', 115200)
valeurs = []

try:
    # On lit les valeurs que l'on stocke dans le tableau valeurs
    while True:
        valeur = float(port.readline())
        valeurs.append(valeur)
        print(valeur)
except KeyboardInterrupt:
    # Lorque le programme est interrompu (CTRL+C), les valeurs sont stockées
    # dans le fichier valeurs.csv
    print('Sauvegarde de valeurs.csv ...')
    np.savetxt('valeurs.csv', np.array(valeurs))
