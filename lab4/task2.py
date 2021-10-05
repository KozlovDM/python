def decorator(func):
    def wrapper(numbers):
        count = func(numbers)
        if count == 0:
            print("Нет")
        elif count > 10:
            print("Очень много")
    return wrapper


@decorator
def count_even_numbers(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1
    return count


count_even_numbers([2, 4, 6, 8])
