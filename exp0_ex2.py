import numpy as np

# 1:10 passos 2
a = np.arange(0, 10, 2)
print(f"Sequência de 0 a 10 com incremento 2: {a}")

# 1:10 passos 1
b = np.arange(1, 5)
print(f"Sequência de 1 a 5: {b}")

#tamanho da matriz v 
print(f"Tamanho de b: {b.shape}")

#vetor v2, de 0 a 10 com 6 elementos
v2 = np.linspace(0, 10, num=6)
print(f"Array de 0 a 10 com 6 elementos: {v2}")