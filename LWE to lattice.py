import numpy as np
import matplotlib.pyplot as plt

def generate_lattice_points(basis, range_vals):
    basis = basis.transpose()
    points = []
    for i in range_vals:
        for j in range_vals:
            point = i * basis[0] + j * basis[1]
            points.append(point)
    return np.array(points)

# Basis vectors
b1 = np.array([3, 2])
b2 = np.array([4, 4])
A = np.array([b1, b2]).transpose()

print("Basis Matrix A:\n", A)

# Vectors s and e
s = np.array([-2, 1])
e = np.array([0.4, -0.6])

w = A @ s
b = w + e

print("Vector b:", b)

# Generate lattice points
range_vals = np.arange(-100, 100)
lattice_points = generate_lattice_points(A, range_vals)

# Plot lattice points and basis vectors
plt.figure(figsize=(8, 8))
ax = plt.gca()

# Scatter plot of lattice points
ax.scatter(lattice_points[:, 0], lattice_points[:, 1], color='black', s=10)

# Plot basis vectors
ax.quiver(0, 0, *b1, color='r', scale=1, scale_units='xy', angles='xy', width=0.004, label='Basis Vectors')
ax.quiver(0, 0, *b2, color='r', scale=1, scale_units='xy', angles='xy', width=0.004)

# Annotate basis vectors
ax.text(b1[0]+0.2, b1[1]+0.2, f'{b1}', color='r', fontsize=12, ha='left')
ax.text(b2[0]-0.2, b2[1]+0.2, f'{b2}', color='r', fontsize=12, ha='right')

# Plot vectors b and w
ax.plot(*b, 'bo', label='Target Vector b')
ax.plot(*w, 'go', label='Closest Lattice Point w')

# Annotate vectors b and w
ax.text(b[0]+0.2, b[1]-0.2, f'{b}', color='b', fontsize=12, ha='left', va='top')
ax.text(w[0]-0.2, w[1]+0.2, f'{w}', color='g', fontsize=12, ha='right')

# Set plot limits and grid
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)
ax.grid(True)

# Add legend
ax.legend()
plt.show()
