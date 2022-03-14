import numpy as np
from numpy import array
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box
import timeit

def gauss(a, b):
    a = a.copy()
    b = b.copy()
    n = len(b)
    x = np.zeros(len(b), dtype=float)

    def forward(a, b):  # Прямой ход
        for k in range(n-1):
            for i in range(k+1, n):
                gss = a[i, k] / a[k, k]
                for j in range(k, n):
                    a[i, j] = a[i, j] - gss*a[k, j]
                b[i] = b[i] - gss*b[k]

    def backward(a, b):   # Обратный ход
        x[n-1] = b[n-1] / a[n-1, n-1]
        for i in range(n-2, -1, -1):
            mtd = b[i]
            for j in range(i+1, n):
                mtd = mtd - a[i, j]*x[j]
            x[i] = mtd/a[i, i]

        return x

    forward(a, b)
    x = backward(a, b)
    return x

a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4  ],
    [2.0, 1.0, 4.0, 3  ]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)

oob_solution = solve_out_of_the_box(a, b)
solution = gauss(a, b)

print(solution)
print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))