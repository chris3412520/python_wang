"""变量并非在程序的任意位置都可以被访问，其访问权限取决于变量定义的位置，/

其所处的有效范围称为变量的作用域。
"""
from pickle import GLOBAL

"""根据作用域的不同，变量可以划分为局部变量和全局变量。
函数内部定义的变量，只能在函数内部被使用
函数执行结束之后局部变量会被释放，此时无法再进行访问。
不同函数内部可以包含同名的局部变量，这些局部变量的关系类似于不同目录下同名文件的关系，它们相互独立，互不影响。
"""
"""全局变量可以在整个程序的范围内起作用，它不会受到函数范围的影响。
"""
"""全局变量在函数内部只能被访问，而无法直接修改。
函数内部只能访问全局变量，而无法直接修改全局变量。
"""
def func():
    x = 10
x=100
func()
print(x)
"""在程序的运行过程中，当自定义函数内某个变量与程序的全局变量使用相同的变量名时，/
程序会优先调用局部变量，屏蔽全局变量。这是因为在函数的局部范围内，局部变量具有更高的优先级。/
程序会先处理函数内的局部变量，而不会影响到全局变量的值。因此"""
"""函数内部无法直接修改全局变量或在嵌套函数的外层函数声明的变量，
但可以使用global或nonlocal关键字修饰变量以间接修改以上变量。
"""
"""使用global关键字可以将局部变量声明为全局变量，其使用方法如下：
global 变量
"""
def func():
   global x
   x = 10
x=100
func()
print(x)

number = 10                    # 定义全局变量
def test_one():
    global number              # 使用global声明变量number为全局变量
    number += 1
    print(number)
test_one()
print(number)
"""使用nonlocal关键字可以在局部作用域中修改嵌套作用域中定义的变量，其使用方法如下：
"""
def test():
    number = 10
    def test_in():
        nonlocal number
        number = 20
    test_in()
    print(number)
test()

def fun(s):
    if len(s) <= 1:
        return s
    else:
        return fun(s[1:])+s[0];
x = "abcde"
print(fun(x))

