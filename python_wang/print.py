"""
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
•    *objects：要打印的一个或多个对象，可以是字符串、变量、表达式等。多个对象之间会根据
sep
参数指定的分隔符进行分隔。
•    sep（可选）：对象之间的分隔符，默认是一个空格
' '。
•    end（可选）：打印结束后添加的字符串，默认是换行符
'\n'。
•    file（可选）：指定输出的文件，默认是标准输出
sys.stdout。
•    flush（可选）：是否立即刷新输出缓冲区，默认是
False。"""
# 打印单个字符串
print("Hello, World!")

# 打印多个对象
name = "Alice"
age = 30
print("Name:", name, "Age:", age)

# 使用自定义分隔符和结束符
print("Hello", "World", sep=", ", end="!\n")

print("hello","world")
t = "A"
if t>="a":
    print(t)
else:
    print("None")
"""	逻辑运算符 and 的工作方式
	•	在 Python 中，and 是短路运算符，它会首先评估左侧的表达式。
	•	如果左侧为 False，整个表达式立即返回 False。
	•	如果左侧为 True，则返回右侧的表达式的值。
具体到 x + y and y % 2：
	•	x + y 结果为 10（True），所以 and 运算符继续评估右侧的 y % 2。
	•	y % 2 结果为 0（False），因此整个表达式的结果是 0。
x + y 计算得到 10，在布尔上下文中为 True。
	•	y % 2 计算得到 0，在布尔上下文中为 False。
	•	x + y and y % 2 由于 x + y 为 True，整个表达式的结果为 y % 2，即 0。
	•	print 函数因此输出 0。"""
"""and 运算符 不一定返回布尔值。它返回的是第一个 False 的操作数，或者如果所有操作数都为 True，则返回最后一个操作数。"""
x=2
y=-2
print(x + y and y % 2)