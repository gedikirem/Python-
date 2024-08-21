import numpy as np

# f'(x) = [f(x+h) - f(x)] / h

func = lambda x: x**2 + 2*x

def derivate(func, x, h=1e-9):
    return (func(x+h) - func(x))/h

print(derivate(func, 1))
# 4.00000033096