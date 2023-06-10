import matplotlib.pyplot as plt
import numpy as np
plt.style.use("classic")

def f(t):
    return t + 1/t

xv = np.linspace(0,6,1000)
yv = f(xv)
plt.plot(xv, yv, lw=1)
plt.xlabel("$z$")
plt.ylabel("$R(z)$")
#plt.grid(True)
plt.ylim(-0.1,7)
#plt.show()

import tikzplotlib
tikzplotlib.clean_figure()
tikzplotlib.save("R_vs_z.tex")
