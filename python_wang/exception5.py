"""else子句可以与try-except语句组合成try-except-else结构，若try监控的代码没有异常，程序会执行else子句后的代码。
try:
    可能出错的代码
except [异常类型 [as error]]:                    # 将捕获到的异常对象赋值error
    捕获异常后的处理代码
else:
    未捕获异常后的处理代码
"""
first_num = int(input("请输入被除数："))
second_num = int(input("请输入除数："))
try:
    res = first_num/second_num
except ZeroDivisionError as error:
    print('异常原因：',error)
else:
    print(res)
