from math import sin

EPS = 10**-6

x = float(input("Donner x en radians : "))

s = 0
terme = x
i = 0

while abs(terme) > EPS:
    s = s + terme
    terme = -terme * x * x / ((2*i + 2) * (2*i + 3))
    i = i + 1

print("Approximation de sin(x) :", s)
print("Valeur de reference :", sin(x))
print("Nombre de termes :", i)
