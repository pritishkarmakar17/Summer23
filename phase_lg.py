import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 150

import numpy as np
import matplotlib.pyplot as plt
from scipy import special

p=int(input("p="))
l=int(input("l="))

# define phi of range 0 to 2*pi
def taninv(x, y):
    return np.angle(x+1j*y)
phi_angle = np.vectorize(taninv)

L= lambda x,p,l: special.assoc_laguerre(x,p,l)

# define phase function on z=0 plane, z_0=1
def R(p,l,r,phi):
    return np.angle(((np.sqrt(2*(r**2)))**(np.abs(l)))*(L(2*(r**2),p,np.abs(l)))*np.exp(1j*(l*phi)))
phase=np.vectorize(R)

a=2
a1=np.linspace(-a,a,500)
xv,yv=np.meshgrid(a1,a1)
zv=phase(p,l,np.sqrt(xv**2+yv**2),phi_angle(xv,yv))
plt.contourf(xv,yv,zv,levels=200,cmap='viridis')
plt.xlabel("x")
plt.ylabel("y")
#plt.colorbar()

#plt.show()
plt.savefig(f"phase_lg{p}{l}.png")
