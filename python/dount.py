import numpy as np
import matplotlib.pyplot as plt

# Function to generate a donut (torus)
def generate_donut():
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, 2 * np.pi, 100)
    theta, phi = np.meshgrid(theta, phi)

    # Torus parametric equations
    R = 2  # Major radius
    r = 1  # Minor radius
    x = (R + r * np.cos(phi)) * np.cos(theta)
    y = (R + r * np.cos(phi)) * np.sin(theta)
    z = r * np.sin(phi)
    return x, y, z

# Plot in Figure 1
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
x, y, z = generate_donut()
ax.plot_surface(x, y, z, color='cyan', edgecolor='k', alpha=0.8)

ax.set_title("3D Donut (Torus)")
plt.show()
