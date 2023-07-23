import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 150

import numpy as np
import matplotlib.pyplot as plt
l=4*10**(-3)
w_0=0.2
z_0=np.pi*w_0**2/l
# define intensity at z_0=1
R=lambda x,z: np.exp(-2*x**2/(w_0**2*(1+z**2/z_0**2)))/(1+z**2/z_0**2)
a1=np.linspace(-50,50,1000)
a2=np.linspace(-1,1,500)
xv,zv=np.meshgrid(a2,a1)
I=R(xv,zv)
plt.contourf(zv,xv,I,levels=200,cmap='Reds')
plt.colorbar()
plt.xlabel("z")
plt.ylabel("x-y plane")

w=lambda z1: w_0*np.sqrt(1+z1**2/z_0**2)
plt.plot(zv,w(zv),'--',color='k',lw=0.8)
plt.plot(zv,-w(zv),'--',color='k',lw=0.8)
plt.ylim(-0.7,0.7)
plt.savefig("intensity_var beamer.png")