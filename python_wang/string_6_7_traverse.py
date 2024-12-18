"""string="hello,world!"
for i in string:
    print(i,sep="， ",end=" ")"""
"""当前代码中的 sep 无效：
	•	在您的代码中，print(i, sep="， ", end=" ") 只传递了一个参数 i 给 print 函数。
	•	当 print 函数只有一个参数时，sep 参数没有作用，因为它用于分隔多个参数。
	•	因此，sep="， " 在这里是多余的，不会影响输出。"""
# 方法一：使用 join 方法
# 使用 '， ' 作为分隔符连接所有字符
string = "hello,world!"
new_string = "，".join(string)
print(new_string)
# 方法二使用解包操作符 * 和 sep 参数
string = "hello,world!"
print(*string, sep="，")
# 方法三
string = "hello,world!"
for i in string:
    print(i, end="，")
print()  # 插入换行

"""拼接字符串"""
first="hello"
second="docker!"
fs=first+second
print(fs)

"""使用len()函数可以获取字符串的长度（即字符的个数）。
"""
print(len(first))

name=input("请输入你的名字：")
print("Hello,"+name+"!")

"""4.2.1 使用%格式化字符串
format表示一个字符串，该字符串中包含单个或多个为真实数据占位的格式符；
values表示单个或多个真实数据；
%代表执行格式化操作，即将format中的格式符替换为values。
字符串中可以包含多个{}符号，字符串被格式化时Python解释器默认会按从左到右的顺序将{}逐个替换为真实的数据
"""
print("%.2f" % 123.444)
name="王源"
age=18
test="{},{}岁，you look absolutely stunning!"
print(test.format(name,age))
"""字符串的{}中可以明确地指定编号，格式化字符串时解释器会按编号取values中相应位置的值替换{}，values中元素的索引从0开始。
"""
name="王源"
age=18
test="{1},{0}岁，you look absolutely stunning!"
print(test.format(age,name))
"""字符串的{}中可以指定名称，字符串在被格式化时Python解释器会按真实数据绑定的名称替换{}中的变量。
"""
name="王源"
age=18
test="{name},{age}岁，you look absolutely stunning!"
print(test.format(name=name,age=age))
"""字符串中的{}可以指定替换的浮点型数据的精度，浮点型数据在被格式化时会按指定的精度进行替换。
"""
points = 19
total = 22
print('所占百分比: {:.2%}'.format(points/total))

"""f-string提供了一种更为简洁的格式化字符串的方式，它在形式上以f或F引领字符串，在字符串中使用“{变量名}”标明被替换的真实数据和其所在位置。
f('{变量名}') 或F('{变量名}')
"""
name="王源"
age=18
test="you look absolutely stunning!"
print(f'{name},{age},{test}')