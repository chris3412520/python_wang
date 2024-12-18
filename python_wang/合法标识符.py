import keyword
import sys
str1 = (input("请输入标识符："))
if keyword.iskeyword(str1):
    print("不是合法标识符")
    sys.exit()
elif str1[0].isdigit() or not str1[0].isalpha() or str1[0] == '_':
    print("不是合法标识符")
else:
    for char in str1[1:]:
        if char.isalnum() or char == '_':
            continue
        else:
            print("不是合法标识符")
            break
    else:
        print("是合法标识符 ")


# if str1.isidentifier():
#     print("是合法标识符")
# else:
#     print("不是合法标识符")

