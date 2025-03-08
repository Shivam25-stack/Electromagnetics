import numpy as np
import matplotlib.pyplot as plt

# Define constants
k = 9e9  # Coulomb's constant (N·m²/C²)

# Define charge positions and values
charges = [
    (0, 1, 1),    # +1C at (0,1)
    (0, -1, 1),   # +1C at (0,-1)
    (1, 0, -1),   # -1C at (1,0)
    (-1, 0, -1)   # -1C at (-1,0)
]

# Define grid
x_range = np.linspace(-2, 2, 20)
y_range = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x_range, y_range)
Ex, Ey = np.zeros(X.shape), np.zeros(Y.shape)

# Compute the electric field
for xq, yq, q in charges:
    dx = X - xq
    dy = Y - yq
    r = np.sqrt(dx**2 + dy**2)
    r[r == 0] = 1e-10  # Avoid division by zero
    Ex += k * q * dx / r**3
    Ey += k * q * dy / r**3

# Normalize for visualization
E_magnitude = np.sqrt(Ex**2 + Ey**2)
Ex /= E_magnitude
Ey /= E_magnitude

# Plot electric field
plt.figure(figsize=(6, 6))
plt.quiver(X, Y, Ex, Ey, color='blue', scale=20)

# Plot charge positions
for xq, yq, q in charges:
    plt.scatter(xq, yq, color='red' if q > 0 else 'blue', s=100)

plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Electric Field of Charge Distribution")
plt.grid()
plt.savefig("../figs/6a.png")
plt.show()
