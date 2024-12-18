def f(n):
    if(n==1):
        return 1
    return n*f(n-1)
print(f(5))
s = lambda m,n:m*n
print(s(6,6))

def fun(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + fun(lst[1:])
x = [1,2,3,4,5]
print(fun(x))


def qh(a, b, c=5):
    return a + b + c
print(qh(5, 10), qh(10, 10, 10))

def add(c):
    d = c.append(40)
    return d
a = [10, 20, 30]
b = add(a)
print(a, b)


def SiBianXing(a, b, c=5, d=8):
    ZhouChang = a + b + c + d
    return ZhouChang

SiBianXing(1,2)

def fun(x):
    if x > 3:
        return x * fun(x-1)
    else:
        return x
print(fun(6))


def f(n):
    n += 1
    return n
x = 10
y = f(x)
print(y)

count = 0
def increment():
         global count
         count += 1
         print("计数器的值:", count)
increment()
increment()
increment()


def myfunc(a, b, c):
    return a + b + c
myfunc(3,2,c=1)

def fun(s):
    if len(s) <= 1:
        return s
    else:
        return fun(s[1:]) + s[0]
x = "abcde"
print(fun(x))


def fun(x, y, **kwargs):
    res = x + y
    for i in kwargs.values():
        res += i
    return res
print(fun(10, 20, A=6, B=1, C=3))

#求两个正方形的面积差
def MianJiCha(a,b):
      s=a**2-b**2
      return s
a=5
b=10
c=MianJiCha(b,a)+a