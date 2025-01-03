"""匿名函数也称为lambda函数，是一种没有函数名的函数。\
它是一种一次性的、在需要的时候定义，用完即丢弃的函数。
"""
"""Python中使用lambda关键字定义匿名函数，它的语法格式如下：
lambda <形式参数列表> :<表达式>
"""
(lambda x: x ** 2)(2)  # 传入一个参数2，返回2的平方
(lambda x, y: x + y)(3, 4)  # 传入两个参数3和4，返回它们的和。
print((lambda x: x ** 2)(2))
print((lambda x,y:x*y)(3,4))

"""匿名函数与普通函数的主要区别如下：
普通函数在定义时有名称，而匿名函数没有名称；
普通函数的函数体中包含有多条语句，而匿名函数的函数体只能是一个表达式；
普通函数可以实现比较复杂的功能，而匿名函数可实现的功能比较简单；
普通函数能被其他程序使用，而匿名函数不能被其他程序使用。
"""
"""定义好的匿名函数最好使用一个变量保存它，以便后期可以随时使用这个函数，然后将该变量作为普通函数调用。
"""
# 定义匿名函数，并将它返回的函数对象赋值给变量temp
temp = lambda x: pow(x, 2)
print(temp(10))
"""通常来说我们会将 lambda 函数作为参数传递给高阶函数（接受其他函数作为参数的函数），
例如 Python 内置函数，如 filter()、map() 或 reduce()等。
 Python 中的 filter() 函数需要两个参数：
定义过滤条件的函数
函数在其上运行的可迭代对象
"""

Ist = [33, 3, 22, 2, 11, 1]
print(filter(lambda x: x > 10, Ist))
