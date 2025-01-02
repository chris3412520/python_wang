
"""2.编写代码，实现将用户输入的十进制整数转换为指定进制（二进制、八进制、十六进制）的功能。
要求分别用到%格式化、format()方法、f-string三种方式进行输出。"""

num=int(input("int:"))
bin_str=bin(num)
print("bin_str:%s"%bin_str)
print("bin_str:{}".format(bin_str))
print(f"bin_str:{bin_str}")
oct_str=oct(num)
print(oct_str)
hex_str=hex(num)
print(hex_str)









"""def convert_number_with_percent():
    num = int(input("请输入一个整数："))

    # 二进制（bin）
    # %b 并不是原生 Python 对数字的格式说明符，这里我们可能手动拼接或直接用 bin(num)
    # 演示手动:
    bin_str = bin(num)[2:]  # 去掉 '0b' 前缀
    print("二进制(%%): %s" % bin_str)

    # 八进制（oct）
    oct_str = oct(num)[2:]  # 去掉 '0o'
    print("八进制(%%): %s" % oct_str)

    # 十六进制（hex）
    hex_str = hex(num)[2:]  # 去掉 '0x'
    print("十六进制(%%): %s" % hex_str)

convert_number_with_percent()"""