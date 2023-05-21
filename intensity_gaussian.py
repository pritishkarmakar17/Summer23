import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 150

import numpy as np
import matplotlib.pyplot as plt

R=lambda r: np.exp(-2*r**2)
a1=np.linspace(-1.7,1.7,200)
xv,yv=np.meshgrid(a1,a1)
zv=R(np.sqrt(xv**2+yv**2))
plt.contourf(xv,yv,zv,levels=100,cmap='viridis')
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar()

theta=np.linspace(0,2*np.pi,500)
x=np.cos(theta)
y=np.sin(theta)
plt.plot( x, y, "--", lw=0.8)

#plt.show()
plt.savefig("intensity.png")