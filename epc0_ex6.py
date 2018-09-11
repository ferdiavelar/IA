import numpy as np
import matplotlib.pyplot as plt
import math as m

def fuzzy(vmax,vrange,size,x):

    a = vmax - vrange
    b = vmax + vrange

    if x <= a:
        return 0
    if x > a and x <= vmax :    
        return (x-a)/(vmax-a)
    if x > vmax and x <= b:    
        return (b-x)/(b-vmax)
    if x > b and x <= size:    
        return 0 

vmax = int(input("Máximo: "))
vrange = int(input("Faixa de valores: "))
size = int(input("Tamanho: "))

x = np.arange(0, size, 0.1)
y=[]

for num in x :
    y.append(fuzzy(vmax,vrange,size,num))

plt.show(plt.plot(x,y))