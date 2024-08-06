import numpy as np
import matplotlib.pyplot as plt


def gram_schmidt(B):
    B = np.array(B, dtype=np.float64)
    n = B.shape[1]
    B_star = np.zeros_like(B)
    for i in range(n):
        B_star[:, i] = B[:, i]
        for j in range(i):
            B_star[:, i] -= np.dot(B[:, i], B_star[:, j]) / np.dot(B_star[:, j], B_star[:, j]) * B_star[:, j]
    return B_star


def babai_nearest_plane(B, t):
    B = np.array(B, dtype=np.float64)
    t = np.array(t, dtype=np.float64)
    B_star = gram_schmidt(B)
    w = np.zeros_like(t)
    e = t.copy()
    n = B.shape[1]

    steps = []

    for i in reversed(range(n)):
        ci = np.round(np.dot(e, B_star[:, i]) / np.dot(B_star[:, i], B_star[:, i]))
        w += ci * B[:, i]
        e -= ci * B[:, i]
        steps.append((w.copy(), e.copy()))

    return w, e, steps


# Example usage
B = np.array([[1, 1], [0, 2]])
t = np.array([2.5, 3.5])
w, e, steps = babai_nearest_plane(B, t)

print(f"w: {w}")
print(f"e: {e}")

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot the basis vectors
origin = np.array([[0, 0], [0, 0]])  # origin point
B = np.array(B)

# First subplot: second last step
w1, e1 = steps[-2]

ax1.quiver(*origin, B[:, 0], B[:, 1], color=['r', 'b'], scale=1, scale_units='xy')
ax1.quiver(0, 0, t[0], t[1], color='g', scale=1, scale_units='xy', label='target t')
ax1.quiver(0, 0, w1[0], w1[1], color='y', scale=1, scale_units='xy', alpha=0.5, label='second last step w')
ax1.quiver(w1[0], w1[1], e1[0], e1[1], color='m', scale=1, scale_units='xy', alpha=0.5, label='second last step e')

ax1.set_xlim(-1, 4)
ax1.set_ylim(-1, 5)
ax1.set_aspect('equal')
ax1.legend()
ax1.grid()
ax1.set_title('Second Last Step')

# Second subplot: final step
w2, e2 = steps[-1]

ax2.quiver(*origin, B[:, 0], B[:, 1], color=['r', 'b'], scale=1, scale_units='xy')
ax2.quiver(0, 0, t[0], t[1], color='g', scale=1, scale_units='xy', label='target t')
ax2.quiver(0, 0, w2[0], w2[1], color='c', scale=1, scale_units='xy', label='final w')
ax2.quiver(w2[0], w2[1], e2[0], e2[1], color='m', scale=1, scale_units='xy', label='final e')

ax2.set_xlim(-1, 4)
ax2.set_ylim(-1, 5)
ax2.set_aspect('equal')
ax2.legend()
ax2.grid()
ax2.set_title('Final Step')

plt.show()
