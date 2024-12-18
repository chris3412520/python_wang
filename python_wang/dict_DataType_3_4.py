"""
一般是用字符串做键

Python中的字典是典型的映射类型。
键必须是唯一的，键必须是不可变类型，可以是整形、浮点型、字符串、元组，而不能是列表或字典类型、集合（集合里的元素不可变）。
字典的值可以是任意类型，值可以重复。
字典像集合一样使用“{}”包裹元素，它也具备类似集合的特点：字典元素无序，，没有索引。"""
d1 = {}
d2 = {1: 1}
d3 = {1.2: 1}
d4 = {(1, 2, 3): 3}
d5 = {"cheng": "wangyuan"}
print(type(d4))

"""使用“{}”可以直接创建字典，还可以使用内置函数dict()创建字典。"""
di1 = dict()
di2 = dict({'A': '123', 'B': '135'})
print(di2)

"""字典的值可通过“键”或内置方法get()访问。"""
dic1 = dict({'A': '123', 'B': '135'})
print(dic1["A"])
print(dic1.get("B"))
"""get方法没有不会报错，返回默认返回值"""
info = {1:'小明', 2:'小黄',3:'小兰'}
name = info.get(4,'小红')
name2 = info.get(1)
print(info)
print(name)
print(name2)
"""字典涉及的数据分为键、值和元素（键值对），除了直接利用键访问值外，
Python还提供了内置方法keys()、values()和items()。
"""
info1 = {'name': 'Jack','age':23,'height':185}
print(info1.keys())
print(info1.values())
print(info1.items())
"""字典支持通过为指定的键赋值或使用update()方法添加或修改元素。
"""
add_dict = {'name': 'Jack','age':23,'height':185}
add_dict['sco'] = 98
add_dict.update({'ces':98})
print(add_dict)

print("=========12.2===========")
"""修改字典元素的本质是通过键获取值，再重新对元素进行赋值。修改元素的操作与添加元素的操作相同。"""
modify_dict = {'name': 'Jack','age':23,'height':185}
modify_dict['name']='cheng'
modify_dict.update({'height':98})
print(modify_dict)
"""Python支持通过pop()、popitem()和clear()方法删除字典中的元素。"""
modify_dict.pop('height')
modify_dict.popitem()
print(modify_dict)
modify_dict.clear()
print(modify_dict)
"""字典推导式的格式、用法与列表推导式类似，区别在于字典推导式外侧为大括号“{}”，且内部需包含键和值两部分。
利用字典推导式可快速交换字典中的键和值。
{new_key:new_value for key,value in dict.items()}
"""
old_dict = {'name': 'Jack','age':23,'height':185}
new_dict = {value:key for key,value in old_dict.items()}
print("new_dict:",new_dict)
"""Zip是Python的内置函数，用于将可迭代对象（如列表、元组、字典等）作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象（注意，返回的其实是一个迭代器）。
"""
"""字典推导式（Dictionary Comprehension） 是一种简洁的方法，用于基于现有的可迭代对象（如列表、元组等）创建字典。
	•	语法结构为 {key_expression: value_expression for item in iterable}。
这是一个循环，遍历列表 numbers 中的每个元素。
	•	num 是循环变量，依次取列表中的值 1、2 和 3。"""
numbers=[1,2,3]
doubled={num:num * 2 for num in numbers}
print(doubled)
names=['Alice','Bob']
ages=[24,30]
name_age={name:age for name,age in zip(names,ages)}
print(name_age)
dict_del = {'name': 'Jack','age':23,'height':185}
del dict_del['age']
print(dict_del)
"""
删除指定的键并返回其对应的值。
value = dict.pop(key[, default])
del dict[key]

"""
"""for x in dic: 这里的 dic 是一个字典，默认遍历的是其键。
	•	print(x, end=" ") 打印的是当前遍历到的键。
	"""
dic_x = {"聊天机器人": "GhatGPT", '搜索引擎': "百度", "浏览器": "Google"}
for x in dic_x:
    print(x, end=" ")
print()
dic_value = {"聊天机器人": "GhatGPT", '搜索引擎': "百度", "浏览器": "Google"}
for value in dic_value.values():
    print(value, end=" ")
print()

print("=========12.3===========")
# 键值对
dict3 = dict([['shuxue', 60], ["yingyu", 70]])
print(dict3)
dict4 = dict([('shuxue', 60), ("yingyu", 70)])
# get方法 直接dict查键报错  用get查不报错
print(dict4)
print(dict4['yingyu'])
dict4.get('yuwen')
a = dict4.get('yuwen', 70)
print(a)
print("================")
d = {"语文": [10, 30, 40, 20], "姓名": ["张三", "jack"]}

info = {1: '小明', 2: '小黄', 3: '小兰'}
name = info.get(4, "小红")
name2 = info.get(1)
print(name, end=',')
print(name2)

print(info)
info[2] = 24
print(info)
info[4] = "小花"
# print(info)
# info.update(3)
s = dict([[1, '3'], [2, '44']])
print(type(s))
print(s.keys())
print(s.pop(1))
print(s.popitem())
print(s.clear())
print("================================")
info = [{"name": "李凯", "gender": "男", 'height': 170}, "wang", ["heng"]]
# info["class"] = "四年级"
print(info)
# print(info.items())
# print(info.keys())
# print(info.values())
# info["name"]="王"
print(info)
# del info["name"]
# info.clear()
# info.pop(0) //错误
print(info)
print(len(info))

print("===============")
"""dict01 = {"cheng": 1, "zhao": 2}
dict02 = {"quan": 3, "de": 4}
dec0102 = dict01.copy()
for key in dict02:
    if key in dec0102:
        dec0102[key] = dec0102[key] + dict01[key]
    else:
        dec0102[key] = dict01[key]
print(dec0102)"""

# l1=l2
# l1.copy



