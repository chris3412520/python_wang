"""根据数据组织方式的不同，Python的组合数据类型可分成三类：序列类型、集合类型和映射类型。
Python中常用的序列类型有字符串（str）、列表（list）和元组（tuple）。
Python中的序列支持双向索引：正向递增索引和反向递减索引。

集合具备确定性、互异性和无序性三个特性。
Python要求放入集合中的元素必须是不可变类型，Python中的整型、浮点型、字符串类型和元组属于不可变类型，列表、字典及集合本身都属于可变的数据类型。
映射类型以键值对的形式存储元素，键值对中的键与值之间存在映射关系。
字典（dict）是Python唯一的内置映射类型，字典的键必须遵守以下两个原则：
每个键只能对应一个值，不允许同一个键在字典中重复出现。

字典中的键是不可变类型。

"""

"""从内容上看，列表可以存储整数、小数、字符串、列表、元组等任何类型的数据
"""
list_one=[]
list_two=['p', 'y', 't', 'h', 'o', 'n']
li_two=list('python')
print(type(li_two))
print(li_two)
"""可迭代对象"""
"""在Python中，支持通过for…in…语句迭代获取数据的对象就是可迭代对象。
学习过可迭代的类型有字符串和列表，后续学习的集合、字典、文件也是可迭代类型的对象。
"""
for char in list_two:
    print(char,end=" ")
print()
"""列表中的元素可以通过索引或切片这两种方式进行访问，也可以使用循环中遍历。
"""
list_three=["Java","C#","Python","PHP"]
print(list_three[1])
print(list_three[1:])
print(list_three[2])
print(list_three[0:2])
print(list_three[2:])
"""列表元素的修改，也是通过下标来实现的。
"""
A = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
A[1] = 'xiaoLu'
"""向列表中添加元素是非常常见的一种列表操作，Python提供了append()、\
extend()和insert()这几个方法向列表末尾、指定位置添加元素。
 append and extend的区别

append整体加入,比如是个列表，就把列表加入到列表中

extend取出加入

insert->指定插入的位置
"""
print("list_four")
list_four=["Java","C#","Python","PHP"]
list_four.extend(["Android", "IOS",])
list_four.append([1,3,4,5])
print(list_four)
list_four.insert(2,"HTML")
print(list_four)
"""列表的排序是将元素按照某种规定进行排列。列表中常用的排序方法有sort()、reverse()和sorted()函数。
"""
print("sort")
lis_one=[6,2,3,5]
"""sort有序的元素会覆盖原来的列表元素，不产生新列表
"""
res=lis_one.sort()
print(lis_one)
"""sorted产生排序后的新列表，排序操作不会对原列表产生影响
"""
lis_two=[6,2,3,5]
res2=sorted(lis_two)
print(lis_two)
"""逆置列表，即把原列表中的元素从右至左依次排列存放  排序操作对原列表产生影响
"""
list_three=[6,2,3,5]
list_three.reverse()
print(list_three)
"""删除列表元素的常用方式有del语句、remove()方法、pop()方法和clear()方法。
"""
"""del 删除列表中指定位置的元素
"""
l = [6, 2, 5, 3, 3]
del l[0]
print(l)
"""remove移除列表中匹配到的第一个元素
"""
l.remove(3)
print(l)
"""pop移除列表中的某个元素，若未指定具体元素，则移除列表中的最后一个元素
"""
"""clear清空列表"""
l.clear()
print(l)