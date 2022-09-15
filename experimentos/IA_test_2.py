import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import seaborn as sb
from IPython.display import display
a1 = np.array((0,0,0))
a2 = np.arange(10)#funciona con numeros enteros
a5 = np.linspace(0,1,11)#permite crear arrays de una dimension de largo n, y que contiene puntos entre a y b distanciado de forma regular. la distancia entre cada punto sera de entre (b-a)/(n-1)
a3 = np.zeros((3,3,3))#crea matrizes 3x3x3 con zeros dentro
a4 = np.ones((3,3,3))#crea matrizes
a6 = np.random.random((3,3,3))#crea matrizes con valores random
#   tupla np.array((0,0,0))
#no tupla np.array(0,0,0)

x = 0
y = 0
a = np.arange(4)
b = np.mean(a)#promedio
c = np.median(a)#mediana
d = np.random.random(10)#crea matriz aleatoria
e = np.percentile(a,40)#percentile
#%%timeit#no se que hace
   #print (a6)
   #display(a3) 
# print("a     =", a)
# print("a + 5 =", a + 5)
# print("a - 5 =", a - 5)
# print("a * 2 =", a * 2)
# print("a / 2 =", a / 2)#division de float
# print("a // 2 =", a // 2)#division entera(division euclidiana)
# print("-a     = ", -a)#inversion
# print("a ** 2 = ", a ** 2)#potencia
# print("a % 2  = ", a % 2)#residuo(modulo)
#print (a5)
#print(a2[:5])#imprime solo los primeros 5 elementos
#print(a2[2:8])#imprime solo los elementos de 2 a 8

display(a3)
#for y in range(0,9):
#    for x in range(0,9):
        #print (a2(x)(y))


