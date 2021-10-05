# coding: utf-8
# license: GPLv3
from python.lab5.task4.enemies import generate_enemy_list
from python.lab5.task4.hero import Hero


def annoying_input_int(message=' '):
    answer = None
    while answer is None:
        try:
            answer = input(message)
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, enemy_list):
    for enemy in enemy_list:
        print('Вышел', enemy)
        while enemy.is_alive() and hero.is_alive():
            print('Вопрос:', enemy.question())
            answer = annoying_input_int('Ответ: ')

            if enemy.check_answer(answer):
                hero.attack(enemy)
                hero.add_experience(1)
                print('Верно! \n** %s кричит от боли **' % enemy)
            else:
                enemy.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
        if enemy.is_alive():
            break
        print('Дракон', enemy)

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero.get_experience())
    else:
        print('К сожалению, Вы проиграли...')


def start_game():
    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами и тролями!')
        print('Представьтесь, пожалуйста: ', end='')
        hero = Hero(input())

        enemy_number = 3
        enemy_list = generate_enemy_list(enemy_number)
        assert (len(enemy_list) == 3)
        print('У Вас на пути', enemy_number, 'врагов!')
        game_tournament(hero, enemy_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
