"""finally子句可以和try-except一起使用，语法格式如下：
try:
    可能出错的代码
except [异常类型 [as error]]:                    # 将捕获到的异常对象赋值error
    捕获异常后的处理代码
finally:
    一定执行的代码
"""
try:
    file = open('./file.txt', mode='r', encoding='utf-8')
    print(file.read())
except FileNotFoundError as error:
    print(error)
finally:
    file.close()
    print('文件已关闭')
