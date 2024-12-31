"""
f = open('test.txt','a')
goal = f.write('先挣它一个亿')
print(goal)
f.close()"""

"""with open('test1.txt','r') as a,open('test2.txt','w') as b:
    b.write(a.read())"""

"""f = open('test.txt','r')
print(f.read(7))
f.close()"""

"""fo = open("test.txt","w")
x= ["大学", "中学", "小学"]
fo.write("\n".join(x))
fo.close()"""

f= open('data.csv', 'r')
print(f.readlines())
f.close()