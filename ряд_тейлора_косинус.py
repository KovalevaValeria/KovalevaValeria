import math

ITERATIONS = 20

def my_cos(x):
    x_pow = 1
    multiplier = 1
    partial_sum = 1
    for n in range(1, ITERATIONS):
        Nam = (2*n + 1)
        x_pow *= x**2
        multiplier *= -1 / (2*n) / (2*n + 1)
        partial_sum += x_pow * multiplier * Nam
    
    return partial_sum

help(math.cos)
help(my_cos)

print(math.cos(0.4))
print(my_cos(0.4))
