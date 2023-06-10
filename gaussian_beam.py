import matplotlib.pyplot as plt
import numpy as np
plt.style.use("classic")

def f(t):
    return np.exp(-2*(t)**2)

xv = np.linspace(-7,7,1000)
yv = f(xv)

plt.plot(xv, yv, lw=1)
plt.xlabel("$r$")
plt.ylabel("$\frac{2I(r)}{c\epsilon_0 \abs(A)^2}$")
plt.grid(True)

import tikzplotlib
tikzplotlib.clean_figure()
tikzplotlib.save("gaussian_beam.tex")
