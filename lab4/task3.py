def swap(func):
    def wrapper(x, y, show):
        func(y, x, show=show)
    return wrapper


@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res


div(2, 4, show=True)
