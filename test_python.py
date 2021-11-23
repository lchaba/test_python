
from math import sqrt


a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
if c == sqrt(a*a + b*b):
    print("треугольник прямоугольный")
else:
    print("треугольник не прямоугольный")

