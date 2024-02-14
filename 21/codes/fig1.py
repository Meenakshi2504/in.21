import numpy as np
import matplotlib.pyplot as plt

# Define the time values
t = np.linspace(0, 2*np.pi, 1000)

# Define the functions
y_t = np.sin(np.pi * t)
x_t = np.sin(np.pi * t - np.pi/2)

# Plot the functions
plt.plot(t, y_t, label='$y(t) = \sin(\pi t)$')
plt.plot(t, x_t, label='$x(t) = \sin(\pi t - \\frac{\pi}{2})$')

# Add labels and legend
plt.xlabel('$t$')
plt.ylabel('$y(t)$ and $x(t)$')
plt.legend()

# Draw a horizontal line at y=0
plt.axhline(0, color='black', linewidth=0.5)

# Set y-axis limits symmetrically around y=0
plt.ylim(-1.1, 1.1)

# Save the figure directly to the relative file path
save_path = '../figs/fig1.png'  # Adjust based on the directory structure
plt.savefig(save_path)

# Display the plot
plt.show()

