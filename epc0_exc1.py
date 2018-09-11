print('Exercicio 1)')
print('#1')
import math 

x = [-1.3 , math.sqrt(3), (1+2+3)*4/5]

print(x)
#######################################################
print("#2")
import math 
from numpy import *

x = [-1.3 , math.sqrt(3), (1+2+3)*4/5]

x = append(x, abs(x[1]))

print(x)

#####################################################

print("#3")
y = [1 , 2, 3, 4]

print(y)

####################################################
print("#4")

#from numpy import *
import math
import numpy as np
from numpy import *

y = [1 , 2, 3, 4]
x = [-1.3 , math.sqrt(3), (1+2+3)*4/5]
x = append(x, abs(x[1]))

print('x+y')
print(x+y)
print('x-y')
print(x-y)
print("y' (transposto)")
yT = np.transpose(y)
print(yT)
print('x*y (elemento a elemento)')
print(np.multiply(x, y))
#multElementos = np.multiply(x,y)
#print(multElementos)
print("x*y' (elemento a elemento)")
print(np.multiply(x, np.transpose(y)))
print('x.*y (np.dot)')
print(np.dot(x,y))
print('x./y (divisao elemento por elemento)')
print(np.divide(x,y))
print('x.^y (exponencial elemento a elemento)')
print(np.power(x, y)) 

z = x + y
print(f"[x y] = {z}")
##########################################################
print('Exercicio 2)')

a = np.arange(0, 10, 2)
print(f"Sequência de 0 a 10 com incremento 2: {a}")

b = np.arange(1, 5)
print(f"Sequência de 1 a 5: {b}")

print(f"Tamanho de b: {b.shape}")

v2 = np.linspace(0, 10, num=6)
print(f"Array de 0 a 10 com 6 elementos: {v2}")
#########################################################
print('Exercicio 3)')
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

###########################################################