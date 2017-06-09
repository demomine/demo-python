def cal(a, b):
    return a + b


print(cal(1, 2))


def calDefault(a, b=10):
    return a + b


print (calDefault(10))


def calTuple(*args):
    for a in args:
        print a


calTuple(1, 2, 3)

sum = lambda a, b, c: a + b + c

print sum(1, 2, 3)



