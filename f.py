def f(x, y):
    z = 2 * x + y
    if z > 5:
        return x
    else:
        raise ValueError('The value of z is too small!')
