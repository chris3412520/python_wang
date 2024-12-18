"""
    author:成照权
    version:0.0.1
    question:创建一个文本文件并输入几行文字，分别使用read()、readline()和readlines()方法读取并输出文件内容。
             分别使用write()和writelines()方法向该文件中追加数据。
"""
#打开文件
file=open('lib12_1.txt','r',encoding='utf-8')
#读写文件
# text=file.read()
#print(text)
# text2=file.readline()
# print(text2)
text3=file.readlines()
print(text3)
#关闭文件

file.close()

# with open('lib12_1.txt',mode='a',encoding='utf-8') as file:
#     file.write("hello,world!\n")

# # 打开文件
# f = open('lib12_1.txt', mode='a', encoding='utf-8')
# # 读写文件（文件每行有换行，加上print还有换行
# f.writelines(["cheng\n", "wangyuan"])
# # 关闭文件
# f.close()