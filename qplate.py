import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 150

import numpy as np
import matplotlib.pyplot as plt
plt.style.use("classic")

q=1

q1=np.pi/2

# define phi of range 0 to 2*pi

f= lambda phi: q*phi + q1

def taninv(x, y):
    return np.angle(x+1j*y)
phi_angle = np.vectorize(taninv)

a=1
a1=np.linspace(-a,a,10)
xv,yv=np.meshgrid(a1,a1)
ax=np.cos(f(phi_angle(xv,yv)))
bx=np.sin(f(phi_angle(xv,yv)))

#zv=f(phi_angle(xv,yv))
#plt.contourf(xv,yv,zv,levels=200,cmap='viridis')
plt.quiver(xv, yv, ax, bx)
#plt.xlabel("x")
#plt.ylabel("y")
#plt.colorbar()

#plt.show()
plt.savefig(f"qplate({q},r).png")