# 1. Import the NUMPY package under the name np.
import numpy as np

# 2. Print the NUMPY version and the configuration.
version = np.__version__
print(f'La versión de numpy es : {version}')

# 3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.random([3, 2, 5])

a1 = np.random.rand(2, 3, 5)

a2 = np.random.randn(2, 3, 5)

# 4. Print a.

print(a)
print(a1)
print(a2)


# 5. Create a 5x2x3 3-dimensional array with all values equaling 1.
# Assign the array to variable "b"

b = np.ones((5, 2, 3))


# 6. Print b.

print(b)

# 7. Do a and b have the same size? How do you prove that in Python code?

print(a.shape)
print(b.shape)

# No tienen el mismo tamaño


# 8. Are you able to add a and b? Why or why not?

# No, porque el numero de columnas de a es diferente al número de filas de b

# 9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to variable "c".

c = b.T

# 10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = np.add(a, c)

# Si, ahora funciona porque el número de columnas de a y el de filas de b son el mismo.

# 11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a, d)

# REVISAR EL POR QUÉ

# 12. Multiply a and c. Assign the result to e.

e = np.multiply(a, c)

# 13. Does e equal to a? Why or why not?

print(e, a)

if e.all() == a.all():
    print('Son iguales')
else:
    print('No son iguales')

# Son iguales porque cualquier matriz por la matriz unitaria es la misma matriz


# 14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = d.max()

d_min = d.min()

d_mean = d.mean()

print(d_max, d_min, d_mean)

# 15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.


f = np.empty((3, 2, 5))

# Ejercicio 16:

for idx in np.ndindex(d.shape):
    value = d[idx]
    if d_min < value < d_mean:
        f[idx] = 25
    elif d_mean < value <= d_max:
        f[idx] = 75
    elif value == d_mean:
        f[idx] = 50
    elif value == d_min:
        f[idx] = 0
    elif value == d_max:
        f[idx] = 100

print(f)

# Ejercicio 17

g = np.empty((3, 2, 5), dtype=str)

for idx in np.ndindex(d.shape):
    value = d[idx]
    if d_min < value < d_mean:
        g[idx] = 'A'
    elif d_mean < value <= d_max:
        g[idx] = 'B'
    elif value == d_mean:
        g[idx] = 'C'
    elif value == d_min:
        g[idx] = 'D'
    elif value == d_max:
        g[idx] = 'E'

print(g)




"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""


"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""



"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""