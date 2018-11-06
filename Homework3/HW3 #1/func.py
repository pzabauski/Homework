from functools import reduce

def x_negated(x):
    return list(map(lambda x: -x, x))


def x_inverted(x):
    return list(map(lambda x: round(1/x, 2), x))


def x_squared(x):
    return list(map(lambda x: x**2, x))


def x_odds(x):
    return list(filter(lambda x: x % 2 == 1, x))


def x_evens(x):
    return list(filter(lambda x: x % 2 == 0, x))


def x_simples(numbers):
    simples = [1, 2, 3, 5, 7]
    for i in range(0, len(numbers)):
        if numbers[i] in simples:
            continue
        else:
            numbers[i] = 0
    return list(filter(lambda x: x > 0, numbers))


def x_sum(x):
    return reduce(lambda x, y: x + y, x)


def x_multiply(x):
    return reduce(lambda x, y: x * y, x)


def x_join(x):
    return reduce(lambda x, y: x*10 + y, x)


def x_unite(x):
    return list(set(x))


def x_reverse(x):
    return x[::-1]
