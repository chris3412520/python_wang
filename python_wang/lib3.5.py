

"""猜数字游戏：由电脑随机产生1-100间整数，给用户5次机会，若猜测的数字大于电脑产生的数字，
提示“很遗憾，你猜大了”；若猜测的数字小于电脑产生的数字时，提示“很遗憾，你猜小了”；
若猜数字的人在规定的次数内猜中设置的数字，提示“恭喜，猜数成功”，否则提示“很遗憾，你的机会用光了”。"""

import random
num=random.randint(1,100)

chance=50
while chance>0:
    my_num = int(input("my_num:"))
    if my_num==num:
        print("恭喜，猜数成功")
        break
    elif my_num>num:
        print("很遗憾，你猜大了")
    else:
        print("很遗憾，你猜小了")
    chance-=1
if chance==0:
    print("很遗憾，你的机会用光了")
