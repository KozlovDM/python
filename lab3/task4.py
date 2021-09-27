import datetime
import time


def decorator(path):
    def log(func):
        def wrapper():
            begin = str(datetime.datetime.now())
            t = time.perf_counter()
            f = func()
            with open(path, "w") as file:
                file.write(
                    begin + "\n" + path + "\n" + ("-" if f is None else f) + "\n" + str((time.perf_counter() - t))
                    + "\n" + str(datetime.datetime.now()))
        return wrapper
    return log


@decorator("C:/Users/user/PycharmProjects/py/python/lab3/log.txt")
def sleep():
    time.sleep(10)


sleep()
