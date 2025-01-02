"""

"""
"""选择结构：

3.输入成绩后先判断成绩是否在0-100之间，如果是，则判断等级，否则输出错误信息。

等级划分如下：成绩不低于85分为“优秀”， 成绩低于85但不低于75为“良好”， 成绩低于75但不低于60为“中等”， 成绩低于60为“差”。"""
scores=int(input("请输入成绩："))
if scores>100 or scores<0:
    print("error")
else:
    print("scores为",scores,"，在0-100之间")
if scores>=85 and scores<=100:
    print("优秀")
elif scores>=75 and scores<85:
    print("良好")
elif scores>=60 and scores<75:
    print("中等")
else:
    if scores<60:
        print("差")
"""score = int(input("请输入成绩："))

# 首先判断是否在合法范围
if score < 0 or score > 100:
    print("错误信息：成绩必须在0~100之间！")
else:
    # 范围合法，进一步根据成绩判断等级
    if score >= 85:
        print("优秀")
    elif score >= 75:
        print("良好")
    elif score >= 60:
        print("中等")
    else:
        print("差")"""

