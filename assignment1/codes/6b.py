import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Coulomb's constant
k = 9e9  # N·m²/C²

# Define charge positions and values
charges = [
    (0, 1, 1),    # +1C at (0,1)
    (0, -1, 1),   # +1C at (0,-1)
    (1, 0, -1),   # -1C at (1,0)
    (-1, 0, -1)   # -1C at (-1,0)
]

# Define grid
x_range = np.linspace(-2, 2, 50)
y_range = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x_range, y_range)

# Compute electric potential
V = np.zeros(X.shape)

for xq, yq, q in charges:
    r = np.sqrt((X - xq) ** 2 + (Y - yq) ** 2)
    r[r == 0] = 1e-10  # Avoid division by zero
    V += k * q / r

# Plot potential in 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, V, cmap='coolwarm')

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("Potential (V)")
ax.set_title("Electric Potential Distribution")
plt.savefig("../figs/6b.png")
plt.show()
