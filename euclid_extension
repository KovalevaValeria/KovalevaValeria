def numeric(a, b):

    q = a // b; r = a - q * b  # первое разложение
    a = b; b = r

    x_2 = 0
    x_1 = 1
    x = 1

    y_2 = 1
    y_1 = -q
    y = -q

    if (b == 0):  # если первое разложение конечно
        return x, y + 1

    while (a % b != 0): # алгоритм Евклида
        q = a // b; r = a - q * b;

        a = b; b = r

        x = -q * x_1 + x_2
        y = -q * y_1 + y_2

        x_2 = x_1; x_1 = x
        y_2 = y_1; y_1 = y

    return x, y

def gcd(a, b):

    while (b != 0):

        a, b = b, a % b 

    return a

test = [(46, 12), (472, 1568), (108, 436)]

for a, b in test:
  x, y = numeric(a, b)
  print(f"{x}*{a} + {y}*{b} = {gcd(a, b)}")
  
