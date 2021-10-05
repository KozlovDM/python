# coding: utf-8
# license: GPLv3
from python.lab5.task4.gameunit import Attacker


class Hero(Attacker):
    __experience = None
    __name = None

    def __init__(self, name):
        super().__init__(100, 50)
        self.__experience = 0
        self.__name = name

    def get_experience(self):
        return self.__experience

    def add_experience(self, count):
        self.__experience += count
