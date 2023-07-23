import matplotlib.pyplot as plt
import numpy as np
plt.style.use("classic")

def f(t):
    return t + 1/t

xv = np.linspace(0,6,1000)
yv = f(xv)
plt.plot(xv, yv, lw=3)
plt.xlabel("$z$")
plt.ylabel("$R(z)$")
#plt.grid(True)
plt.ylim(-0.1,7)
tics=[0,1,2,3,4,5,6]
plt.xticks(tics, ["$0$","$z_0$","$2z_0$","$3z_0$","$4z_0$","$5z_0$","$6z_0$"] )
plt.savefig("R_vs_z beamer.png")

#import tikzplotlib
#tikzplotlib.clean_figure()
#tikzplotlib.save("R_vs_z.tex")
