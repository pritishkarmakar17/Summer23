import matplotlib.pyplot as plt
import numpy as np
plt.style.use("classic")

xv = np.linspace(-10,10,1000)
yv = np.arctan(xv)
plt.plot(xv, yv, lw=1)
plt.xlabel("$z/z_0$")
plt.ylabel("$\phi_g$")
tics=[-np.pi/2,-np.pi/4, 0 ,np.pi/4, np.pi/2]
plt.yticks(tics, ["$-\pi/2$","$-\pi/4$",0,"$\pi/4$","$\pi/2$"] )
#plt.grid(True)


#plt.show()
import tikzplotlib
tikzplotlib.clean_figure()
tikzplotlib.save("gouy.tex")


