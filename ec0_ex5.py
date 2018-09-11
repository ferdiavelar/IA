import numpy as np
import matplotlib.pyplot as plt

def func1(inicio, incremento, fim):
    x = np.arange(inicio, fim, incremento)
    y = np.sin(x) * np.exp(x)
    plt.plot(x, y)
    plt.title("Gráfico exemplo - II")
    plt.grid(True)
    plt.show()

func1(-2 * np.pi, 0.1, 2 * np.pi)