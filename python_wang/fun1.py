"""函数是组织好的、实现单一功能或相关联功能的代码段。\
我们可以将函数视为一段有名字的代码，这类代码可以在需要的地方以“函数名()”的形式调用。
"""
from sympy.solvers.diophantine.diophantine import length


# 打印正方形的函数
def print_triangle(lenth):
    for i in range(lenth):
        for i in range(lenth):
            print("*", end=" ")
        print()

# 使用函数，打印边长为两个星号的正方形
print_triangle(2)
print_triangle(3)
print_triangle(4)
"""函数式编程具有以下优点：
将程序模块化，既减少了冗余代码，又让程序结构更为清晰。
提高开发人员的编程效率
方便后期的维护与扩展
"""
"""前面使用的print()函数和input()都是Python的内置函数，这些函数由Python定义。开发人员也可以根据自己的需求定义函数，Python中使用关键字def来定义函数，其语法格式如下：
"""


def add():
    result = 11 + 22
    print(result)


def add_modify(a, b):
    result = a + b
    return result


"""函数在定义完成后不会立刻执行，直到被程序调用时才会执行。
语法格式如下：函数名([参数列表])
1. 程序在调用函数的位置暂停执行。
2. 将数据传递给函数参数。
3. 执行函数体中的语句。
4. 程序回到暂停处继续执行。
"""
"""函数在定义时可以在其内部嵌套定义另外一个函数，此时嵌套的函数称为外层函数，被嵌套的函数称为内层函数。
"""


def add_modify(a, b):
    result = a + b
    print(result)

    def test():
        print("我是内层函数")


add_modify(10, 20)
"""我们通常将定义函数时设置的参数称为形式参数（简称为形参），将调用函数时传入的参数称为实际参数（简称为实参）。函数的参数传递是指将实际参数传递给形式参数的过程。
函数参数的传递可以分为：
位置参数传递
关键字参数传递
默认参数传递
参数的打包与解包
混合传递
"""
"""函数在被调用时会将实参按照相应的位置依次传递给形参，\
也就是说将第一个实参传递给第一个形参，将第二个实参传递给第二个形参，以此类推。
"""


def get_max(a, b):
    if a > b:
        print(a, "是较大的值！")
    else:
        print(b, "是较大的值！")


get_max(8, 5)
"""关键字参数的传递是通过“形参=实参”的格式将实参与形参相关联，\
将实参按照相应的关键字传递给形参。
"""


def connect(ip, port):
    print(f"设备{ip}:{port}连接！")


connect(ip="127.0.0.1", port=8080)
"""函数在定义时可以指定形参的默认值，\
如此在被调用时可以选择是否给带有默认值的形参传值，\
若没有给带有默认值的形参传值，则直接使用该形参的默认值。
"""


def connect(ip, port=8080):
    print(f"设备{ip}:{port}连接")


connect(ip="127.0.0.1")
connect(ip="127.0.0.1", port=3316)
"""打包
如果函数在定义时无法确定需要接收多少个数据，\
那么可以在定义函数时为形参添加“*”或“**”：
“*” —— 接收以元组形式打包的多个值
“**”—— 接收以字典形式打包的多个值
虽然函数中添加“*”或“**”的形参可以是符合命名规范的任意名称，\
但这里建议使用*args和**kwargs。
若函数没有接收到任何数据，参数*args和**kwargs为空，\
即它们为空元组或空字典。

"""


def test(*args):
    print(args)


test(11, 22, 33, 44, 55)


def test(**kwargs):
    print(kwargs)


test(a=11, b=22, c=33, d=44, e=55)

"""解包
实参是元组   →  可以使用“*”拆分成多个值  →  按位置参数传给形参
实参是字典   →  可以使用“**” 拆分成多个键值对  →   按关键字参数传给形参
"""


def test(a, b, c, d, e):
    print(a, b, c, d, e)


nums = (11, 22, 33, 44, 55)
test(*nums)


def test(a, b, c, d, e):
    print(a, b, c, d, e)
nums={"a":11, "b":22, "c":33, "d":44, "e":55}
test(**nums)
"""前面介绍的参数传递的方式在定义函数或调用函数时可以混合使用，\
但是需要遵循一定的规则，具体规则如下：
  优先按位置参数传递的方式。
  然后按关键字参数传递的方式。
  之后按默认参数传递的方式。
  最后按打包传递的方式。

"""
"""在定义函数时：
带有默认值的参数必须位于普通参数之后。
带有“*”标识的参数必须位于带有默认值的参数之后。
带有“**”标识的参数必须位于带有“*”标识的参数之后。
"""
def test(a,b,c=33,*args,**kwargs):
    print(a,b,c,args,kwargs)
test(1,2)
test(1,2,3)
test(1,2,3,4)
test(1,2,3,4,e=5)

def add(a, b=5):
    print('In function:a={},b={}'.format(a, b))
    return a + b
c = add(3)
print(c)

def many_param(num_one, num_two, *args):
    print(args)
many_param(11, 22, 33, 44, 55)
"""函数中的return语句会在函数结束时将数据返回给程序，同时让程序回到函数被调用的位置继续执行。
"""
def filter_sensitive_words(words):
    if "山寨" in words:
        new_words = words.replace("山寨", "**")
    return new_words
result = filter_sensitive_words("这个手机是山寨版吧！")
print(result)
"""如果函数使用return语句返回多个值，那么这些值将被保存到元组中。
"""
def move(x,y,step):
    nx=x+step
    ny=y-step
    return nx,ny
result = move(100,100,60)
print(result)