""" Module for solution of Duffing Oscillator """
import numpy as np
from scipy import integrate
from matplotlib import pyplot as plt

def diff_eq(_X, t):
    """ Differential equation """
    x, y = _X
    _dx = y
    _dy = gamma*np.cos(w*t) - alpha*x - beta*x**3 - delta*y
    return[_dx, _dy]

alpha = 1   # spring ratio
beta = 1         # nonlinear restoring force
delta = 1     # damping
gamma = 1      # amplitude
w = 1          # frequency
X = [np.random.uniform(0.5, 1), np.random.uniform(0.5, 1)]
# Solve for the trajectories
tspan = np.linspace(0, 500, 400000)
x_t = integrate.odeint(diff_eq, X, tspan)
dx = x_t[:,0]
dy = x_t[:,1]
lines = plt.plot(dx, dy, ms=1)
plt.setp(lines, linewidth=0.5)
plt.show()