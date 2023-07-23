import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 150

import numpy as np
import matplotlib.pyplot as plt

w_0=0.2
l=4*10**(-3)
z_0=np.pi*w_0**2/l
k=2*np.pi/l
# define intensity 
R=lambda x,z: np.exp(-x**2/(w_0**2*(1+z**2/z_0**2)))/np.sqrt(1+z**2/z_0**2)*(np.sin(np.arctan(z/z_0)-0.5*x**2* k/(z+z_0/z)-k*z))
a1=np.linspace(-50,50,1000)
a2=np.linspace(-1,1,500)
xv,zv=np.meshgrid(a2,a1)
I=R(xv,zv)
plt.contourf(zv,xv,I,levels=100,cmap='bwr')
plt.colorbar()
plt.xlabel("z")
plt.ylabel("x-y plane")



plt.savefig("Rad of cur beamer.png")