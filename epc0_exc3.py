
import math
import numpy as np
import matplotlib.pyplot as plt

a = np.random.rand(1000)

m = np.mean(a)
std = np.std(a)

print(f"Média: {m}")
print(f"Desvio Padrão: {std}")

t = np.arange(0, 2 * np.pi, 0.001)

y = np.sin(t)
plt.plot(t, y)
plt.grid(True)
plt.show()

m = np.ones((1, 1000))
print(f"Tamanho de m: {m.size}")