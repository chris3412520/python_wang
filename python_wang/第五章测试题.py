tup2=(114,5,14,191,9810)
print(tup2[3])
print(tup2[2:])
print(tup2[1:-2])
print(tup2[2:3])

numbers=[1,2,3,4]
numbers.append([5,6,7,8])
print(numbers)
print(len(numbers))

a=("apple","banana","orange","banana","pear")
print(a.index("banana"))

ls=[2023,'Happy',['Good','Luck']]
print(ls[2][1])

a=[3,9,5]
b=a
b[0]=7
print(b)

info = {1:'小明', 2:'小黄',3:'小兰'}
info[4] = '小红'
info[2] = '小白'
print(info)

ls=[20,30,50,10,90]
"""ls.remove(-1)"""
"""del ls[-1]"""
ls.remove(ls[-1])
'''ls.pop(-1)'''
print(ls)

mylist=['Failure','is','the','mother','of','success']
for x in mylist[:]:
    if len(x)<=3:
        mylist.append(x)
print(mylist)

lista=[1,2,3,4,5,6,7,8,9,10]
s=0
for i in range(0,len(lista),2):
   s=s+lista[i]
print("s=",s)

ls=[0,'',{},None,(),[],'empty']
print(len(ls))

score={'跳绳':85,'跳远':99,'跑步':92}
score['跳绳']=95
print(score)


dic={(12,34,'a'):'a','a':5678}
print(type(dic))

a={123:'a','a':123}
print(type(a))

datas={'Name':'XiaoMing','No':'1001','Age':'14','School':'ShiYan XueXiao'}
print(len(datas))

d1={'学科':'语文','班级':'2班','最高分':99}
d2={'学科':'数学','班级':'2班','最高分':100}
d1.update(d2)
print(d1)

tup1 = ('苏炳添', '谷爱凌', '北京冬奥会', '2022')
tup2 = (201, 8, 4, 21, 155, 255, 22 )
print (tup1[-1::-2],sum(tup2))

tup=('python',2022,'神州十三号')
print(type(tup))

# 列表示例
my_list = [1, 2, 3, 4, 5]
sliced_list = my_list[1:3]  # 输出: [2, 3]
print(sliced_list)

# 元组示例
my_tuple = (1, 2, 3, 4, 5)
sliced_tuple = my_tuple[1:3]  # 输出: (2, 3)
print(sliced_tuple)

a=[33,55,22,77]
a.sort(reverse = True)
for i in a:
  print(i)

"""20. (单选题) 给定字典d，哪个选项对x in d的描述是正确的?( )
A
判断x是否是在字典d中以键或值方式存在
在Python中，表达式 x in d 仅检查 x 是否是字典 d 的 键（keys），而不会检查其是否为值（values）。因此，x in d 不会判断 x 是否作为值存在于字典中。
B
判断x是否是字典d中的键

C
x是一个二元元组，判断x是否是字典d中的键值对

D
判断x是否是字典d中的值"""