h = []
h.extend("code")
print(h)

list_one = [1, 'hello', [3, ], 3.14]
print(len(list_one))


h = [1, 2, 4, 5]
h.insert(3, 2)
print(h)

h = [1,2,3,4,5]
a = h.pop(1)
# print(a)
print(h[-a])

print([i for i in range(1, 101) if i % 2 != 0])
print([ord(char) for char in "hello"])
print([(e, f) for e in range(3) for f in range(3)])

"""a = input("请输入a")
# n=input("请输入n")
list1 = [a * i for i in range(1, 10)]
print("+".join(list1))
"""
s1 = ['alex', 'li', 'WuSir', 'super', 'ab']
# s = []

print([i ** 2 for i in range(1, 51) if i % 3 == 0])

# str1=input("请输入：")

# sum min remove

list6 = [80, 67, 89, 78, 90]
t = tuple(list6)
print(t)
print(type(t))

ss = set(list6)
print(type(ss))

sss = [1, 2, 4, 1, 2, 4]
s4 = set(sss)
sss_ = list(s4)
print(s4)
print(sss_)
print("===================")
s5={}
print(s5)
print(type(s5))

s6=set()

