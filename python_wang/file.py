def f(x, y=5):
    print(x + y)
f(10)

def f(a,*b):
    for n in b:
        a*=n
    return a
print(f(1,2,3,4))

def foo(a):
    return a+10
def bar(b):
    return b*2
result = bar(foo(5))
print(result)
"""在函数内修改列表，列表都是指向同一个地址，都是指向同一个列表"""
def multiply_numbers (numbers):
    result =1
    for number in numbers:
        result *= number
    return result
numbers = [1, 2, 3, 4, 5]
result = multiply_numbers(numbers)
print (result)

n=1
def f(x,y):
    n=2
    return x*y
print(n,f(2,4))


n=1
def f(x,y):
    global n
    n=2
    return x*y
print(n,f(2,4))

"""操作系统以文件为单位对数据进行管理。
文件标识的意义：找到计算机中唯一确定的文件。
文件标识的组成：文件路径、文件名主干、文件扩展名。
根据数据的逻辑存储结构，人们将计算机中的文件分为文本文件和二进制文件。
文本文件：基于字符编码、专门存储文本字符数据。
"""
""""文本文件支持多种编码方式，不同编码方式下字符与字节的对应关系不同，
常见的编码方式以及字符与字节的对应关系如表所示。
"""
"""二进制文件：基于值编码，指定某个值是什么意思。
不能直接使用文字处理程序正常读写，必须先了解其结构和序列化规则，
再设计正确的反序列化规则，才能正确获取文件信息。
"""
"""内置函数open()用于打开一个已经存在的文件，或者创建一个新文件，该方法的声明如下：
open(filename, mode='r', encoding=None)
filename：要打开的目标文件名的字符串（可以包含文件具体路径）。
mode：设置文件的打开模式，取值有r、w、a。
encoding：设置文件的编码格式, 推荐使用UTF-8。
r：以只读方式打开文件（mode参数的默认值）。
w：以只写方式打开文件。
a：以追加方式打开文件。
b：以二进制形式打开文件。
+：以更新的方式打开文件（可读可写）重点

"""

"""2.关闭文件
Python可通过close()方法关闭文件，也可以使用with语句实现文件的自动关闭。
with语句会清理
file.close()
with语句可预定义清理操作，以实现文件的自动关闭。
with open('a.txt') as f:
        pass
7.2.2 文件的读写
Python提供了一系列读写文件的方法，包括读取文件的read()、readline()、readlines()方法和写文件的write()、writelines()方法，下面结合这些方法分别介绍如何读写文件。

"""
"""file1=open("python_wang\\demo.txt",mode='w',encoding='utf-8')
with open('file.txt', mode='r') as f:
    print(f.read(2))   						# 读取两个字节的数据
    print(f.read())    						# 读取剩余的全部数据"""
#打开文件
f=open('demo.txt',mode='r',encoding='utf-8')
#读写文件（文件每行有换行，加上print还有换行
text=f.readlines()
for line in text:
    print(line,end="")
print()
for line in f:
    print(line,end="")
print()
#text2=f.readline()
print(text)
#print(text2)
#关闭文件
f.close()


"""read()（参数缺省时）和readlines()方法都可一次读取文件中的全部数据，
但因为计算机的内存是有限的，若文件较大，read()和readlines()的一次读取便会耗尽系统内存，
所以这两种操作都不够安全。
为了保证读取安全，通常多次调用read()方法，每次读取size字节的数据。
"""
"""写文件——write()方法
"""
with open('demo.txt',mode='a',encoding='utf-8') as f:
    f.write("hello,world!\n")
"""writelines()方法
writelines()方法用于将一个字符串列表写入文件，每个列表元素被视为一行数据，但是不会自动添加换行符。
其语法格式如下：writelines(lines)
参数lines表示要写入文件中的数据，该参数可以是一个字符串或者字符串列表。
若写入文件的数据在文件中需要换行，需要显式指定换行符。
"""
"""
write方法用于将单个字符串写入文件，可以写入任何类型的数据，但需要将数据转换为字符串。如果要将多个数据写入文件，需要多次调用write方法。
writelines方法用于将多个字符串写入文件，需要传入一个字符串列表作为参数。writelines会一次性将列表中的所有字符串写入文件，效率比多次调用write高。
"""
#打开文件
f=open('demo.txt',mode='a',encoding='utf-8')
#读写文件（文件每行有换行，加上print还有换行
f.writelines(["cheng\n","wangyuan"])
#关闭文件
f.close()

with open('lzy.txt',mode='r',encoding='utf-8') as f1,open('lzy(b).txt',mode='w',encoding='utf-8') as f2:
    for line in f1:
        if line[-2:]=='备份':
            break


"""7.2.3 文件的定位读写
在文件的一次打开与关闭之间进行的读写操作是连续的，程序总是从上次读写的位置继续向下进行读写操作。
每个文件对象都有一个称为“文件读写位置”的属性，该属性会记录当前读写的位置。
文件读写位置默认为0，即在文件首部。
Python提供了一些获取与修改文件读写位置的方法，以实现文件的定位读写。
tell()：获取文件当前的读写位置。
seek()：控制文件的读写位置。
"""

