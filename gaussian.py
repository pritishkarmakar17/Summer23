import matplotlib.pyplot as plt
import numpy as np
plt.style.use("classic")

def f(t):
    return np.exp(-(t)**2/2)/(np.sqrt(2*np.pi))

xv = np.linspace(-7,7,1000)
yv = f(xv)

plt.plot(xv, yv, lw=1)
plt.xlabel("$t$")
plt.ylabel("$f(t)$")
plt.grid(True)

import tikzplotlib
tikzplotlib.clean_figure()
tikzplotlib.save("gaussian.tex")
