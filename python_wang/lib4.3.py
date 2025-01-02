
"""3.分别用for和while语句遍历输出字符串“helloworld”中的字符；"""
s='helloworld'
for i in s:
    print(i,end="")
print()
j=0
while j<len(s):
    print(s[j],end="")
    j+=1





"""def traverse_hello_while():
    s = "helloworld"
    i = 0
    while i < len(s):
        print(s[i], end=" ")
        i += 1
    print()

# traverse_hello_while()"""