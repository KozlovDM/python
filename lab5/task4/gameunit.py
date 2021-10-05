# coding: utf-8
# license: GPLv3


class Attacker:
    __health = None
    __attack = None

    def __init__(self, health, attack):
        self.__health = health
        self.__attack = attack

    def attack(self, target):
        target.__health -= self.__attack

    def is_alive(self):
        return self.__health > 0
