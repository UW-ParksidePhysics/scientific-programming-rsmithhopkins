import numpy as np
import matplotlib.pyplot as plt

t = 0
a = [0.5, 1, 2]
f = 3
k = 3 * np.pi
w = 3 * np.pi

def wave_fxn(x, a, f, k, w, t):
    return np.exp(-((a * x - f * t) ** 2)) * np.sin(k * x - w * t)

x = np.linspace(-4, 4, 400)

plt.plot()
for alpha in a:
    y = wave_fxn(x, a, t, f, k, w)
