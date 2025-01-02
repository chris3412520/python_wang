def add(c):
    d = c.append(40)

    return d


a = [10, 20, 30]

b = add(a)

print(a, b)


def fun(s):
    if len(s) <= 1:
        return s
    else:
        return fun(s[1:])+s[0];
x = "abcde"
print(fun(x))


def fun(x, y, **kwargs):
    res = x + y
    for i in kwargs.values():
        res += i
    return res


print(fun(10, 20, A=6, B=1, C=3))


def MianJiCha(a, b):
    s = a ** 2 - b ** 2
    return s


a = 5
b = 10
c = MianJiCha(b, a) + a