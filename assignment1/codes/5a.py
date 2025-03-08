import numpy as np
import matplotlib.pyplot as plt

# Define phi from -2π to 2π
phi = np.linspace(-2*np.pi, 2*np.pi, 500)

# Compute |F|
F_magnitude = np.sqrt(38 + 24 * (np.sin(phi) + np.cos(phi)))

# Plot
plt.figure(figsize=(8, 5))
plt.plot(phi, F_magnitude, label=r'$\left|\vec{F}\right| = \sqrt{38 + 24(\sin\phi + \cos\phi)}$', color='b')

# Labels and title
plt.xlabel(r'$\phi$ (radians)')
plt.ylabel(r'$\left|\vec{F}\right|$')
plt.title(r'Plot of $\left|\vec{F}\right|$ vs. $\phi$')

# Add grid and legend
plt.grid()
plt.legend()
plt.savefig("../figs/5a.png")
plt.show()
