import math # Импорирет библиотеку
import numpy # Импортирует библиотеку
import matplotlib.pyplot as mpp # Импортирует библиотеку
# Эта программа рисует график функции, заданной выражением ниже
if __name__=='__main__': # Эта часть будет работать только если программа запущена на прямую
    arguments = numpy.arange(0, 200, 0.1) # Данная строка вводит функцию от 0 до 200 с шагом 0,1
    mpp.plot(
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments] # Здесь введена функция с учетом вышеназванных условий
    )
    mpp.show() # Эта строка выводит график на экран
