import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 50, 500)
y = np.sin(x) * np.exp(-x / 5)

plt.plot(x, y)
plt.title("A Damped Oscillation")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show(block=True)
