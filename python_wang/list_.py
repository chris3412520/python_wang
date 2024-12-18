"""列表推导式是符合Python语法规则的复合表达式，\
它用于以简洁的方式根据已有的列表构建满足特定需求的列表。
[exp for x in list]
列表推导式还可以结合if判断语句或for循环嵌套，生成更灵活的列表。
"""
Ls1 =[a**2 for a in [1,2,3,4,5,6] ]
Ls2 = [ord(char) for char in "hello"]
Ls3 = [x for x in range(1,100) if x % 2 ==0]
Ls4= [(e, f) for e in range(3) for f in range(3)]
print(Ls1)
print(Ls2)
print(Ls3)
print(Ls4)