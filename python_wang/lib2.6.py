"""6.一个最简单的计算器，支持 +,-,*,/ 四种运算。仅需考虑输入输出为整数的情况，数据和运算结果不会超过 int 表示的范围。然而：

    如果出现除数为0的情况，则输出：Divided by zero!。

    如果出现无效的操作符（即不为 +,-,*,/ 之一），则输出：Invalid operator!。

    除号表示整除，结果向 0 取整。"""
a=int(input("a:"))
op=input("operator:")
b=int(input("b:"))

if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    if b==0:
        print("Divided by zero!")
    else:
        print(a/b)
else:
    print("Invalid operator!")