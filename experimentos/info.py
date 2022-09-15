#Importar la librería
import numpy as np

a1 = np.array([1,2,3])                 # con una lista
type(a1)

numpy.ndarray

a2 = np.arange(10)                 # np.arange es un metodo similar al range del tipo list

a2

array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

a3 =  np.zeros((2,3))                 # crear un lista de dos dimensiones, pre-rellenada con zeros
a4 =  np.ones((2,3))                 # crear un lista de dos dimensiones, pre-rellenada con unos

from IPython.display import display
display(a3);display(a4)

array([[ 0.,  0.,  0.],
       [ 0.,  0.,  0.]])

array([[ 1.,  1.,  1.],
       [ 1.,  1.,  1.]])

np.linspace(a,b,n) es una función que permite crear arrays de una dimensión, de largo n, y que contienen puntos entre a y b, distanciados de forma regular. La distancia entre cada punto sera de
.

a5 = np.linspace(0,1,11)
display(a5)

array([ 0. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9,  1. ])

# Dtypes
a5.dtype

dtype('float64')

Dimensión de un Array

display(a1)

array([1, 2, 3])

a1.shape                 # dimensión

(3,)

display(a3)

array([[ 0.,  0.,  0.],
       [ 0.,  0.,  0.]])

a3.shape                   # dimensión

(2, 3)

a1D = np.array([1,2,3])
a2D = np.array([[1,2,3]])
display(a1D.shape)
display(a2D.shape)

(3,)

(1, 3)

# Son los dos arrays iguales?
np.array_equal(a1D,a2D)

False

# Reshaping
new_dims = (1,a1D.shape[0])
a = a1D.reshape(new_dims)

np.array_equal(a,a2D)

True

Acceso a elementos y Slicing

a = np.array([[1,0,3],[4,3,5],[6,10,-1]])
a

array([[ 1,  0,  3],
       [ 4,  3,  5],
       [ 6, 10, -1]])

a[2,1]

10

Para acceder a un elemento de un array de dimensión n, la síntaxis es
.
En este curso y frecuentemente en ML trabajaremos con arrays de dimensión 1 o dimensión 2, por lo que:

    Para un array de 1D: 

Para un array de 2D:

a = np.arange(10)
b = np.eye(3)
display(a);display(b)

array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

array([[ 1.,  0.,  0.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])

a[:5]

array([0, 1, 2, 3, 4])

b[0:3,1]

array([ 0.,  1.,  0.])

b[2,0:3]

array([ 0.,  0.,  1.])

b[:,:]

array([[ 1.,  0.,  0.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])

# Slicing de arrays

                      # 5 primeros elementos del array a
                      # esta notación nos permite obtener la segunda línea del array b
                      # tercera columna del array b
                      # todo el array b.

Operaciones sobre arrays

# Aritmetica
a = np.arange(4)

print("a     =", a)
print("a + 5 =", a + 5)
print("a - 5 =", a - 5)
print("a * 2 =", a * 2)
print("a / 2 =", a / 2)
print("a // 2 =", a // 2)  
print("-a     = ", -a)
print("a ** 2 = ", a ** 2)
print("a % 2  = ", a % 2)

a     = [0 1 2 3]
a + 5 = [5 6 7 8]
a - 5 = [-5 -4 -3 -2]
a * 2 = [0 2 4 6]
a / 2 = [ 0.   0.5  1.   1.5]
a // 2 = [0 0 1 1]
-a     =  [ 0 -1 -2 -3]
a ** 2 =  [0 1 4 9]
a % 2  =  [0 1 0 1]

Operator 	ufunc
+ 	np.add
- 	np.subtract
* 	np.multiply

# Otras ufuncs interesantes
a = np.arange(4)
b = np.arange(1,5)

display(np.exp(a))         # exponencial
display(np.log(b))         # logaritmo natural
display(np.sqrt(a))        # raiz cuadrada
display(np.greater(a,b))   # superior o igual punto a punto

array([  1.        ,   2.71828183,   7.3890561 ,  20.08553692])

array([ 0.        ,  0.69314718,  1.09861229,  1.38629436])

array([ 0.        ,  1.        ,  1.41421356,  1.73205081])

array([False, False, False, False], dtype=bool)

a

array([0, 1, 2, 3])

b

array([1, 2, 3, 4])

Rendimiento
Las ufuncs corren a velocidad de código compilado C.
De poder utilizarse se deberían preferir a el uso de for loops.
Un código Numpy solo con funciones nativas, sin bucles, se le llama código "vectorizado".

import numpy as np

%%timeit
a = np.arange(1000000)
b = np.zeros(1000000)
i = 0
for el in a:
    b[i] = el+el
    i+=1

237 ms ± 14.3 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%%timeit
a = np.arange(1000000)
a+a

1.61 ms ± 56.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
a+a

NameErrorTraceback (most recent call last)
<ipython-input-6-253a555a051d> in <module>()
----> 1 get_ipython().run_cell_magic('timeit', '', 'a+a')

/opt/conda/lib/python3.5/site-packages/IPython/core/interactiveshell.py in run_cell_magic(self, magic_name, line, cell)
   2101             magic_arg_s = self.var_expand(line, stack_depth)
   2102             with self.builtin_trap:
-> 2103                 result = fn(magic_arg_s, cell)
   2104             return result
   2105 

<decorator-gen-61> in timeit(self, line, cell)

/opt/conda/lib/python3.5/site-packages/IPython/core/magic.py in <lambda>(f, *a, **k)
    185     # but it's overkill for just that one bit of state.
    186     def magic_deco(arg):
--> 187         call = lambda f, *a, **k: f(*a, **k)
    188 
    189         if callable(arg):

/opt/conda/lib/python3.5/site-packages/IPython/core/magics/execution.py in timeit(self, line, cell)
   1078             for index in range(0, 10):
   1079                 number = 10 ** index
-> 1080                 time_number = timer.timeit(number)
   1081                 if time_number >= 0.2:
   1082                     break

/opt/conda/lib/python3.5/site-packages/IPython/core/magics/execution.py in timeit(self, number)
    158         gc.disable()
    159         try:
--> 160             timing = self.inner(it, self.timer)
    161         finally:
    162             if gcold:

<magic-timeit> in inner(_it, _timer)

NameError: name 'a' is not defined

Estadística y aleatoridad

# Estadística
a = np.arange(10)

display(np.mean(a))           # promedio
display(np.median(a))         # mediana         

4.5

4.5

np.percentile(a,40)                  # percentil

3.6000000000000001

np.random.random(10) # Aleatoridad

array([ 0.24532752,  0.19727378,  0.70780713,  0.77635632,  0.6175905 ,
        0.17239969,  0.41967961,  0.66742302,  0.8488295 ,  0.60224365])

