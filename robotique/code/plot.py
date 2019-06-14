import serial
import time
import matplotlib.pyplot as plt

# Ouverture de la ligne série 115200 bauds
port = serial.Serial('/dev/ttyUSB0', 115200)

# Création de la figure de dessin
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.ion()
line1, = ax.plot([], [])

xs = []
ys = []
k = 0
lastPlot = time.time()
while True:
    # Lecture et stockage de la valeur
    valeur = float(port.readline())
    k += 1
    xs.append(k)
    ys.append(valeur)

    # A 20hz, mise à jour du plot
    if time.time()-lastPlot > 0.05:
        lastPlot = time.time()
        # Valeurs en X et en Y
        line1.set_xdata(xs)
        line1.set_ydata(ys)
        # Bornes du dessin
        plt.xlim(min(xs)*0.9, max(xs)*1.1)
        plt.ylim(min(ys)*0.9, max(ys)*1.1)
        plt.pause(0.001) # Nécessaire pour mettre à jour le dessin
