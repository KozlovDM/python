from statistics import mean, stdev

# список чисел
numbers = []
# заполняем список
while True:
    number = input()
    if number == 'End':
        break
    numbers.append(int(number))

numbers.sort()
print('максимум: ', numbers[len(numbers) - 1])
print('минимум: ', numbers[0])
print('среднее: ', mean(numbers))
print('среднеквадратичное отклонение : ', stdev(numbers))

