#Statistics: Mean

from sympy import symbols, Sum, IndexedBase
from sympy.abc import i, n

# Define an indexed variable
x = IndexedBase('x')

# Define the expression for mean
expr = Sum(x[i], (i, 1, n)) / n

print(expr)

