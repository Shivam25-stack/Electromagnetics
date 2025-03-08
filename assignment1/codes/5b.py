import numpy as np
import matplotlib.pyplot as plt

# Define s from -10 to 10 (adjust range as needed)
s = np.linspace(-10, 10, 500)

# Compute |F|
F_magnitude = np.sqrt((40 / (s**2 + 1) + 3 * np.sqrt(2))**2 + 4)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(s, F_magnitude, label=r'$\left|\vec{F}\right| = \sqrt{\left(\frac{40}{s^2 + 1} + 3\sqrt{2} \right)^2 + 4}$', color='b')

# Labels and title
plt.xlabel(r'$s$')
plt.ylabel(r'$\left|\vec{F}\right|$')
plt.title(r'Plot of $\left|\vec{F}\right|$ vs. $s$')

# Add grid and legend
plt.grid()
plt.legend()
plt.savefig("../figs/5b.png")
plt.show()
