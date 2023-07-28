import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 150

import numpy as np
import matplotlib.pyplot as plt


l=int(input("l="))

# define phi of range 0 to 2*pi
def taninv(x, y):
    return np.angle(x+1j*y)
phi_angle = np.vectorize(taninv)


# define phase function on z=0 plane, z_0=1
def phase(phi):
    return l*phi%(2*np.pi)


a=2
a1=np.linspace(-a,a,500)
xv,yv=np.meshgrid(a1,a1)
zv=phase(phi_angle(xv,yv))
plt.contourf(xv,yv,zv,levels=300,cmap='Greys')
plt.xlabel("x")
plt.ylabel("y")
ticks = [0,np.pi,2*np.pi-0.001]
cbar = plt.colorbar( ticks=ticks)
cbar.set_ticklabels(['$0$', '$\pi$', '$2\pi$'])

#plt.show()
plt.savefig(f"cgh_l{l}.png")

