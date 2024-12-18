# =============================================================================
# 作者: 成照权
# 日期: 2024-11-26
# 提取用户输入的字符串中的英文字母和数字，分别存放在两个列表中。
#    要求英文字母不区分大小写，重复字母和数字只记一次。
#    最后输出统计的所有英文字母和数字。
# =============================================================================
# str1 = input("请输入一个字符串: ")
# letter = set()
# alpha = set()
# for char in str1:
#     if char.isalpha():
#         letter.add(char.lower())
#     elif char.isdigit():
#         alpha.add(char)
# alpha_list = sorted(list(letter))
# digit_list = sorted(list(alpha))
# print("英文字母列表：", alpha_list)
# print("数字列表：", digit_list)

print(list(range(1, 5)))
fruit = ['a', 'b', 'c']
fruit.insert(2, 'd')
print(fruit)
list1 = [1, 3, 2, 5, 7, 8, 9]
print("====")
list1.sort()
print(list1)
t1 = ([1, 2], 3, 4)
t1[0][0] = 0
print(t1)
ls1 = [1, 1.1, 3.1, 4]
del ls1[1:3]
print(ls1)
my_numbers = [3, 1, 5, 2, 4]
result = []
for i in range(len(my_numbers)):
    result.append(my_numbers[i] ** 2)
print(result)
print([i ** 2 for i in [3, 1, 5, 2, 4]])
a = (1, 'a', [2, 'b'])
print(type(a))
print("====================================")
s1 = ['cheng', 'zhao', 'Ruquan', 'IF']
s = [i.upper() for i in s1 if len(i) >= 3]
print(s)
print("=====")
"""for i in range(0,51):
    if i%3==0 :
        i**2"""
st = [i ** 2 for i in range(1, 51) if i & 3 == 0]
print(st)
ss={1,3}
ss.add(4)
print(ss)
sd={"y":1}
print(type(sd))
