# 输入一行字符，统计输出字符串中包含数字、字母、空格和其他字符的个数
input1 = input("请输入一行字符：")

# 初始化计数器
count_shuzi = 0
count_zimu = 0
count_space = 0
count_others = 0

for char in input1:
    if char.isdigit():
        count_shuzi += 1
    elif char.isalpha():
        count_zimu += 1
    elif char.isspace():
        count_space += 1
    else:
        count_others += 1

print("数字个数：", count_shuzi)
print("字母个数：", count_zimu)
print("空格个数：", count_space)
print("其他字符个数：", count_others)
