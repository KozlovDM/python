import math

SQRT5 = math.sqrt(5)

n = int(input())
p = (SQRT5 + 1) / 2
print(int(p ** n / SQRT5 + 0.5))
