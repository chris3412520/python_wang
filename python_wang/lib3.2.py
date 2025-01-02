
"""找到并输出所有的水仙花数，分别用while和for语句实现。(水仙花数是指一个3位数，它的每个位上的数字的3次幂之和等于它本身)
"""
num = 100
while num < 1000:
    hundred = num // 100
    ten = (num // 10) % 10
    one = num % 10
    if (hundred**3+ten**3+one**3)==num:
        print(num)
    num += 1








"""def narcissistic_while():
    num = 100
    while num < 1000:
        hundreds = num // 100       # 百位
        tens = (num // 10) % 10     # 十位
        ones = num % 10            # 个位
        if (hundreds**3 + tens**3 + ones**3) == num:
            print(num)
        num += 1

narcissistic_while()"""
