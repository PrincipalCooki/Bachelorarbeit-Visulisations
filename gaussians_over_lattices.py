import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def gaussian_2d(x, y, mu=0, sigma=2):
    return np.exp(-((x - mu)**2 + (y - mu)**2) / (2 * sigma**2))


range_val = 5
step = 0.5
x = np.arange(-range_val, range_val + step, step)
y = np.arange(-range_val, range_val + step, step)
x, y = np.meshgrid(x, y)

z = gaussian_2d(x, y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(x, y, z, c=z, cmap='viridis')

colorbar = plt.colorbar(scatter, ax=ax, pad=0.1)
colorbar.set_label('Gaussian Value')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Discrete Gaussian Distribution over 2D Lattice')

plt.show()
