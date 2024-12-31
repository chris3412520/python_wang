"""%s（字符串占位符）：
	•	用途：用于插入字符串（str）类型的变量。实际上，%s 可以插入任何类型的变量，因为它会将变量转换为字符串形式。"""
name='阿宝'
age=10
hobby='编程'
print('我的名字叫%s，我今年%d岁了，我的爱好是%s。'%(name,age,hobby))
print('我的名字叫%s，我今年%s岁了，我的爱好是%s。'%(name,age,hobby))

test1="chengchris"
test2=test1[5:]*3
print(test2)

string='WangYuan,you look absolutely stunning!'
print(string.split(',',2))
print(len(string))

print('-'.join(string))