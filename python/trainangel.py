import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Create Figure 1
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')

# Define vertices of the 3D triangle
vertices = [
    [0, 0, 0],   # Point A
    [1, 0, 0],   # Point B
    [0, 1, 1]    # Point C
]

# Create triangle from vertices
triangle = [[vertices[0], vertices[1], vertices[2]]]

# Add to 3D plot
ax.add_collection3d(Poly3DCollection(triangle, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.7))

# Set axes limits for better view
ax.set_xlim([-1, 2])
ax.set_ylim([-1, 2])
ax.set_zlim([-1, 2])

plt.show()
