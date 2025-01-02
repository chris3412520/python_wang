
"""4.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。"""

line=input("str_line:")
is_alpha=0
is_space=0
is_digit=0
is_other=0

for i in line:
    if i.isalpha():
        is_alpha+=1
    elif i.isspace():
        is_space+=1
    elif i.isdigit():
        is_digit+=1
    else:
        is_other+=1
print(f"is_alpha:{is_alpha}",f"is_space:{is_space}",f"is_digit:{is_digit}",f"is_other:{is_other}")













"""def count_chars():
    line = input("请输入一行字符：")

    count_alpha = 0
    count_space = 0
    count_digit = 0
    count_other = 0

    for ch in line:
        if ch.isalpha():
            count_alpha += 1
        elif ch.isspace():
            count_space += 1
        elif ch.isdigit():
            count_digit += 1
        else:
            count_other += 1

    print(f"英文字符个数: {count_alpha}")
    print(f"空格个数: {count_space}")
    print(f"数字个数: {count_digit}")
    print(f"其它字符个数: {count_other}")

count_chars()"""