import numpy as np
import matplotlib.pyplot as plt

dez = np.loadtxt("datos.dat")
dcero=dez[0]
lon=len(dcero)
x=np.linspace(1,lon,lon)

plt.figure(figsize=(15,5))
plt.subplot(121)
plt.imshow(dez)
plt.colorbar(label="Desplazamiento")
plt.axis('equal')
plt.ylabel("Indice D")
plt.xlabel("Indice X")
plt.subplot(122)
for i in range(100):
    di=dez[i]
    plt.plot(x,di)
plt.ylabel("Desplazamiento")
plt.xlabel("Indice X")
plt.savefig("imagenes.png")