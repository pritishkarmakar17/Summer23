import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 150

import numpy as np
import matplotlib.pyplot as plt
from scipy import special

L= lambda x,p,l: special.assoc_laguerre(x,p,l)

p=int(input("p="))
l=int(input("l="))

R=lambda p,l,x,y: ((np.sqrt(2*(x**2+y**2)))**(2*np.abs(l)))*(L(2*(x**2+y**2),p,np.abs(l)))**2*np.exp(-2*(x**2+y**2))
a=2.5
a1=np.linspace(-a,a,200)
xv,yv=np.meshgrid(a1,a1)
zv=R(p,l,xv,yv)
plt.contourf(xv,yv,zv,levels=300,cmap='viridis')
plt.xlabel("x")
plt.ylabel("y")
#plt.colorbar()

#plt.show()
plt.savefig(f"intensity_lg{p}{l}.png")
