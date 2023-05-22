import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 150

import numpy as np
import matplotlib.pyplot as plt
from scipy import special

H=lambda n: special.hermite(n, monic=False)

m=int(input("m="))
n=int(input("n="))

R=lambda m,n,x,y: (H(m)(np.sqrt(2)*x)*H(n)(np.sqrt(2)*y))**2*np.exp(-2*(x**2+y**2))
l=2
a1=np.linspace(-l,l,200)
xv,yv=np.meshgrid(a1,a1)
zv=R(m,n,xv,yv)
plt.contourf(xv,yv,zv,levels=100,cmap='viridis')
plt.xlabel("x")
plt.ylabel("y")
#plt.colorbar()

#plt.show()
plt.savefig(f"intensity_hg{m}{n}.png")
