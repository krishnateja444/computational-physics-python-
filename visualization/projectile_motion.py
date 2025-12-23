import numpy as np
import matplotlib.pyplot as plt

v0 = 20
theta = np.pi / 4
g = 9.8

t = np.linspace(0, 3, 100)
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

plt.plot(x, y)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Projectile Motion")
plt.show()
