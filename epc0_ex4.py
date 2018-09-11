import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)

y = np.sin(x) * np.exp(x)

# gráfico
plt.plot(x, y)

#título
plt.title("Gráfico Exemplo")

#grade
plt.grid(True)

#figura
plt.show()