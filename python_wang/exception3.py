"""try-except语句可以捕获与处理程序的单个、多个或全部异常。
"""

try:
    num_one = int(input("请输入被除数："))
    num_two = int(input("请输入除数："))
    print("结果为", num_one / num_two)
except (ZeroDivisionError, ValueError) as error:
    print("出错了，原因：", error)
