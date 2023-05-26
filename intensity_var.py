import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 150

import numpy as np
import matplotlib.pyplot as plt

# define intensity at z_0=1
R=lambda x,z: np.exp(-2*x**2/(1+z**2))/(1+z**2)
a1=np.linspace(-1.5,1.5,500)
a2=np.linspace(-3,3,500)
xv,zv=np.meshgrid(a2,a1)
I=R(xv,zv)
plt.contourf(zv,xv,I,levels=100,cmap='viridis')
plt.colorbar()
plt.xlabel("z")
plt.ylabel("x-y plane")

w=lambda z1: np.sqrt(1+z1**2)
plt.plot(zv,w(zv),"--",lw=0.7)
plt.plot(zv,-w(zv),"--",lw=0.7)

plt.show()