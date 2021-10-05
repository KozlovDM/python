# coding: utf-8
# license: GPLv3
from random import randint, choice

from python.lab5.task4.gameunit import Attacker


def generate_random_enemy():
    random_enemy_type = choice(enemy_types)
    enemy = random_enemy_type()
    return enemy


def generate_enemy_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Enemy(Attacker):
    __answer = None
    __quest = None

    def __init__(self, health, attack, color):
        super().__init__(health, attack)
        self.__color = color

    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer.lower() == self.__answer.lower()

    def question(self):
        pass


class GreenDragon(Enemy):
    def __init__(self):
        super().__init__(200, 10, 'Зелёный')

    def __str__(self):
        return "Зелёный дракон"

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + ' + ' + str(y)
        self.set_answer(str(x + y))
        return self.__quest


class RedDragon(Enemy):
    def __init__(self):
        super().__init__(200, 10, 'Красный')

    def __str__(self):
        return "Красный дракон"

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + ' - ' + str(y)
        self.set_answer(str(x - y))
        return self.__quest


class BlackDragon(Enemy):
    def __init__(self):
        super().__init__(200, 10, 'Черный')

    def __str__(self):
        return "Черный дракон"

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + ' * ' + str(y)
        self.set_answer(str(x * y))
        return self.__quest


class GreenTroll(Enemy):
    def __init__(self):
        super().__init__(200, 10, 'Зелёный')

    def __str__(self):
        return "Зелёный троль"

    def question(self):
        x = randint(1, 5)
        self.__quest = "Угадай число от 1 до 5"
        self.set_answer(str(x))
        return self.__quest


class RedTroll(Enemy):
    def __init__(self):
        super().__init__(200, 10, 'Красный')

    def __str__(self):
        return "Красный троль"

    def question(self):
        x = randint(1, 504)
        self.__quest = "Число простое " + str(x) + " ?"
        self.set_answer("Да" if self.__is_prime(x) else "Нет")
        return self.__quest

    @staticmethod
    def __is_prime(n):
        d = 2
        while d * d <= n and n % d != 0:
            d += 1
        return d * d > n


class BlackTroll(Enemy):
    def __init__(self):
        super().__init__(200, 10, 'Черный')

    def __str__(self):
        return "Черный троль"

    def question(self):
        x = randint(1, 500)
        self.__quest = "Разложи число на простые множители " + str(x)
        self.set_answer(self.get_prime_nums(x))
        return self.__quest

    @staticmethod
    def get_prime_nums(n):
        i = 2
        prime_nums = ""
        while i * i <= n:
            while n % i == 0:
                prime_nums += str(i) + ", "
                n = n / i
            i = i + 1
        if n > 1:
            prime_nums += str(i)
        return prime_nums


enemy_types = [RedDragon, RedTroll, GreenDragon, GreenTroll, BlackDragon, BlackTroll]
