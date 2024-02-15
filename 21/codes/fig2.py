import numpy as np
import matplotlib.pyplot as plt

# Transfer function H(jw)
def H(jw):
    return (1j * jw - np.pi) / (1j * jw + np.pi)

# Frequency range
omega = np.linspace(0, 2 * np.pi, 1000)

# Calculate |H(jw)| for each frequency
magnitude_H = np.abs(H(omega))

# Plotting
plt.plot(omega, magnitude_H, label=r'$|H(j\omega)|$')
plt.scatter(np.pi, np.abs(H(np.pi)), color='red', label=r'Mark at $\omega = \pi$')
plt.xlabel(r'$\omega$')
plt.ylabel(r'$|H(j\omega)|$')
plt.legend()
plt.grid(True)
# Save the figure directly to the relative file path
save_path = '../figs/fig2.png'  # Adjust based on the directory structure
plt.savefig(save_path)
plt.show()

