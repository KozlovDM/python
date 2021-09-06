from math import sqrt

# список чисел
numbers = []
for i in range(1, 2500, 10):
    num = sqrt(i)
    if int(num) == num:
        numbers.append(i)
print(numbers)
