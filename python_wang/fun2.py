def exchange(a, b):
    a, b = b, a
    print(a, b)


a, b = 3, 5
exchange(a, b)
print(a, b)


def f(n):
    n = n * 2
    return n


a = [7, 1]
b = f(a)
print(a, b)


def f(x):
    color = ["红", "橙", "黄", "绿", "青", "蓝", "紫"]

    def lucky(x, y):
        n = x + y
        return n

    m = x * int(lucky(5, 6)) % 7
    print("幸运颜色是:", color[m])


f(5)


def area(r, pi=3.14):
    return r * r * pi


print(area(3, 10))


def fun(x, y, **kwargs):
    res = x + y
    for i in kwargs.values():
        res += i
    return res


print(fun(10, 20, A=6, B=1, C=3))


def vol(length, width, height):
    v = length * width * height
    return v

"""
s = vol(3, 7, width=4)
print(s)"""
"""多学一招：调用其他模块中的函数
import导入模块
模块名.函数名（）调用
编写函数保存为py文件
将要导入的、自己编写的py文件跟当前文件放在同一目录里

在Python中，__main__是一个特殊的名字，用于表示顶层代码运行环境的名称。\
当一个Python文件被直接运行时，它的__name__变量会被设置为__main__\
。这意味着你可以通过检查__name__ == '__main__'\
来判断代码是作为主程序运行还是被导入到其他模块中。

"""
def printstar():
    print("**********")
#测试
if __name__ == '__main__':
    printstar()
