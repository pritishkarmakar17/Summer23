import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 150

import numpy as np
import matplotlib.pyplot as plt

R=lambda r: np.exp(-r**2/2)
a1=np.linspace(-3.5,3.5,200)
xv,yv=np.meshgrid(a1,a1)
zv=R(np.sqrt(xv**2+yv**2))
plt.contourf(xv,yv,zv,levels=100,cmap='viridis')
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar()


plt.show()