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
