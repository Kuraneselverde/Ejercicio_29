import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D, get_test_data
from matplotlib import cm

dez = np.loadtxt("datos.dat")
plot = plt.figure(figsize=(15,7))
ax = plot.add_subplot(1, 2, 1, projection='3d')
X, Y = np.mgrid[0:dez.shape[0], 0:dez.shape[1]]
surf=ax.plot_surface(X/100, Y/100, dez ,rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.ylabel("Posicion [metros]")
plt.xlabel("Tiempo [segundos]")

plot.colorbar(surf, shrink=0.5, aspect=5)

ay = plot.add_subplot(1, 2, 2)
dcero=dez[0]
dfin=dez[-1]
lon=len(dcero)
x=np.linspace(1,lon,lon)
plt.plot(x/100,dcero,label="tiempo inicial")
plt.plot(x/100,dfin,label="tiempo final")
plt.ylabel("Desplazamiento [metros]")
plt.xlabel("Posicion [metros]")
plt.legend()
plt.savefig("IMG19.png")