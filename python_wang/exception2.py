num_one = int(input("请输入被除数："))
num_two = int(input("请输入除数："))
try:
    print("结果为", num_one / num_two)
except ZeroDivisionError as error:
    print("出错了，原因：", error)
