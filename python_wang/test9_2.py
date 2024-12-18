"""2.有如下成绩列表[11,22,33,44,55,66,77,88,99,90],
 将所有大于等于60的值保存至字典的第一个key中，将小于60值保存至第二个key的值中。"""
list1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
dic = {">=60": [], "<60": []}
# for list1 in range(0,len(list1)):
for i in list1:
    if i >= 60:
        dic[">=60"].append(i)
    else:
        dic["<60"].append(i)
print(dic)


