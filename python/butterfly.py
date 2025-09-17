import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # for 3D plotting

# 1. Parameter t (acts like "time" or angle)
t = np.linspace(0, 24 * np.pi, 5000)

# 2. Butterfly radial function r(t)
r = np.exp(np.cos(t)) - 2 * np.cos(4 * t) - (np.sin(t/12))**5

# 3. Parametric x, y (in 2D plane)
x = np.sin(t) * r
y = np.cos(t) * r

# 4. Fix z = 0 (one layer in XY plane)
z = np.zeros_like(t)

# 5. Plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, linewidth=0.8)

ax.set_title("Butterfly Curve (One Layer in 3D)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# Show nice angle
ax.view_init(elev=30, azim=120)
plt.show()
