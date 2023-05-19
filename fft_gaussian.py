import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(t):
    return np.exp(-(t)**2/2)/(np.sqrt(2*np.pi))

def ft(y):
    int_re = lambda t: f(t)*np.sin(y*t)
    int_im = lambda t: f(t)*np.cos(y*t)
    g_re = quad(int_re,-np.inf,np.inf)[0]/(2*np.pi)
    g_im = quad(int_im,-np.inf,np.inf)[0]/(2*np.pi)
    return g_re - 1j*g_im
g = np.frompyfunc(ft, 1, 1)

xv = np.linspace(-7,7,1000)
yv = np.abs(g(xv))
plt.plot(xv, yv, lw=1)
plt.xlabel("$\omega$")
plt.ylabel("$abs(g(\omega))$")
plt.grid(True)
 
import tikzplotlib
tikzplotlib.clean_figure()
tikzplotlib.save("fft_gaussian.tex")


