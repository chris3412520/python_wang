"""Python中提供了实现字符串查找操作的find()方法，该方法可查找字符串中是否包含子串，若包含则返回子串首次出现的位置，否则返回-1。
str.find(sub[, start[, end]])
sub：指定要查找的子串。

start：开始索引，默认为0。

end：结束索引，默认为字符串的长度。

"""
test="wang yuan,you look absolutely stunning!"
name="wang yuan"
name2="cheng zhao quan"
result=test.find(name[0])
print(result)

"""Python中提供了实现字符串替换操作的replace()方法，该方法可将当前字符串中的指定子串替换成新的子串，并返回替换后的新字符串。
str.replace(old, new[, count])
old：被替换的旧子串。

new：替换旧子串的新子串。

count：表示替换旧字符串的次数。
在 Python 中，反斜杠（\）被用作续行符，用于将一行代码拆分成多行，\
以提高代码的可读性和可维护性。具体到字符串中，\
反斜杠用于将一个长字符串分成多行书写，而不会在字符串中插入实际的换行符。
Python 还支持自动字符串连接，即在圆括号内或在同一行中直接书写相邻的字符串字面量，\
Python 会自动将它们连接起来。因此，上述代码中的反斜杠在某些情况下是可选的，\
具体取决于代码的书写方式
"""
string = 'He said, "you have to go forward, '\
'Then turn left, Then go forward, and Then turn right."'
# 指定替换两次
new_string = string.replace("Then", "then",2)
print(new_string)

"""split()方法可以按照指定分隔符对字符串进行分割，该方法会返回由分割后的子串组成的列表。
str.split(sep=None, maxsplit=-1)
sep：分隔符，默认为空字符。
maxsplit：分割次数，默认值为-1 表示不限制分割次数。
maxsplit也就是分割几次，比如maxsplit=2,即会根据sep分割几次

"""
test_split="wang yuan,you look absolutely stunning!"
result_split=test_split.split(sep=",", maxsplit=-1)
print(result_split)

"""join()方法使用指定的字符连接字符串并生成一个新的字符串。join()方法的语法格式如下。
str.join(iterable)
iterable --可迭代数据，简单理解就是字符串string、列表list、元组tuple、字典dict、集合set。
而且每个参与迭代的元素必须是字符串类型，不能包含数字或其他类型。

"""
symbol = '-'
world = ["Python","Java"]
print(symbol.join(world))

time="2021-12-01"
res=time.split(sep="-")
new_time="/".join(res)
print(new_time)

"""字符串中前后可能会包含一些无用的字符（如空格），\
在处理字符串之前往往需要先删除这些无用的字符。\
Python中的strip()、lstrip()和rstrip()方法可以删除字符串中的指定字符或字符串。
"""
test_transform="cheng zhao quan"
test_transform2="CHENG ZHAO QUAN"
print(test_transform.upper())
print(test_transform2.lower())
print(test_transform.capitalize())
print(test_transform.title())
"""count方法：统计字符串中某个子字符串的个数
"""
test_count="chengzhaoquan"
count1=test_count.count("n")
print(count1)
count2=test_count.count("n",6)
print(count2)
"""index方法：检测字符串是否包括子字符串
如果包含子字符串则返回开始的索引值，否则抛出异常

"""
print(test_count.index("a"))