import numpy as np
import matplotlib.pyplot as plt

# Given parameters
H = 3.5  # Wave height in meters
T = 9    # Wave period in seconds
g = 9.81 # Acceleration due to gravity in m/s^2

# Calculate wavelength
L = (g * T**2) / (2 * np.pi)

# Define time array
t = np.linspace(0, 4*T, 1000)

# Calculate the sinusoidal wave
y = H * np.sin((2 * np.pi / T) * t)

# Plot the wave
plt.plot(t, y)

plt.xlabel('Time (s)')
plt.ylabel('Amplitude (m)')
plt.grid(True)

# Save the plot as PDF
plt.savefig('plot.png')

# Show the plot
plt.show()


