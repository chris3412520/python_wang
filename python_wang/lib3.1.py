
"""循环结构
石头剪刀布游戏：使用Python实现一个简单的石头剪刀布游戏，
让你可以与计算机进行对战。用数字代表——   0: "石头",    1: "布",     2: "剪刀"。
"""
import random

num = random.randint(0, 2)
game = {0: "石头", 1: "布", 2: "剪刀"}

my_num=int(input("switch(0 or 1 or2):"))
print("机器人",game[num])
print("人",game[my_num])
if my_num==num:
    print("equal")
elif (my_num==0 and num==2)or(my_num==1 and num==0)or(my_num==2 and num==1):
    print("victory")
else:
    print("danger")
