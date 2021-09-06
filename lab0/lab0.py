def lab0():
    # результат храним тут
    friends = 0
    fans = 0
    idols = 0

    # количество подписок
    N = int(input())
    # список подписок
    subscriptions = []
    # заполняем список подписок
    for i in range(N):
        subscriptions.append(input())

    # количество подписчиков
    M = int(input())
    # идем по подписчикам и определяем кем они являются
    for i in range(M):
        current_subscriber = input()
        # проверка на друга, если друзья убираем из списка подписок и переходим к следущему подписчику
        if current_subscriber in subscriptions:
            friends += 1
            subscriptions.remove(current_subscriber)
            continue
        # проверка на поклонников
        if not current_subscriber in subscriptions:
            fans += 1
    # остальные люди в подписках являются кумирами
    idols = len(subscriptions)

    print(friends, fans, idols)


lab0()
