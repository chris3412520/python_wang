import itertools
for i in "CHINA":
    for j in range(2):
        if i=='A':
            continue
        print(i,end="")

"""for i in "CHINA":
    for j in range(2):
        print(i,end="")
         if i=='A':
            break"""

s=0
for i in range(1,101):
    s+=i
    if i==4:
        print(s)
        break

for i in itertools.count():
    print(i,end=' ')
    if i ==10:
        break

s = 0
for i in range(1,101):
      s += i
else:
      print(1)

for i in range(1,20):
    if i%3==0:
        break
    else:
        print(i,end=' ')

print()

sum = 0
for i in range(10):
    if i % 2 == 0:
        sum = sum + i
print(sum)

su=0
for i in [0,2,4,6,8]:
    su+=i
    print(su,end=' ')
print()
print(su)

for i in "python":
    if i=='n':
        continue
    print(i,end=',')
print("n")
