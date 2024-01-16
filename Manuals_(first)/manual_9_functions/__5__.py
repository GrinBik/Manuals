def square(a, b):
    value = a * b
    return value


def cube(num):
    result = square(num, num) * 6
    return result


print(cube(3))
