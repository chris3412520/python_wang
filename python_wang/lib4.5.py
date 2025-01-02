
"""5.判断一个数是否是回文数。"""
s=input("line:")
if s==s[::-1]:
    print("是回文数")
else:
    print("no")











"""
def is_palindrome_number():
    num_str = input("请输入一个整数：")
    # 方法1: 判断字符串反转后是否相同
    if num_str == num_str[::-1]:
        print(f"{num_str} 是回文数")
    else:
        print(f"{num_str} 不是回文数")

# is_palindrome_number()"""