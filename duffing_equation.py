""" Module for solution of Duffing Oscillator """
import numpy as np
from scipy import integrate
from matplotlib import pyplot as plt
import ast

def diff_eq(_X, t):
    """ Differential equation """
    x, y = _X
    _dx = y
    _dy = gamma*np.cos(w*t) - alpha*x - beta*x**3 - delta*y
    return[_dx, _dy]

if __name__ == '__main__':
    alpha = 1   # spring ratio
    beta = 1         # nonlinear restoring force
    delta = 1     # damping
    gamma = 1      # amplitude
    w = 1          # frequency
    while True: 
        print('1 -> Change factors, 2 -> Show oscillator_lines, q -> Quit')
        choose = input()
        if choose == '1':
            alpha = ast.literal_eval(input("alpha = "))
            beta = ast.literal_eval(input("beta = "))
            delta = ast.literal_eval(input("delta = "))
            gamma = ast.literal_eval(input("gamma = "))
            w = ast.literal_eval(input("w = "))
        if choose == '2':
            X = [np.random.uniform(0.5, 1), np.random.uniform(0.5, 1)]
            # Solve for the trajectories
            tspan = np.linspace(0, 500, 400000)
            x_t = integrate.odeint(diff_eq, X, tspan)
            dx = x_t[:,0]
            dy = x_t[:,1]
            lines = plt.plot(dx, dy, ms=1)
            plt.setp(lines, linewidth=0.5)
            plt.title(F'alpha = {alpha} beta = {beta} delta = {delta} gamma = {gamma} w = {w}')
            plt.show()
        if choose == 'q':
            break