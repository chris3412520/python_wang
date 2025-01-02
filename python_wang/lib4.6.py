"""




6.输入一个带后缀的文件名，如abc.docx，根据后缀名判断该文件是不是word文档。

"""
filename=input("put(.docx or .doc):")
if filename.endswith('.docx') or filename.endswith('.doc'):
    print("yes")
else:
    print("no")















"""# 输入一个带后缀的文件名，如abc.docx，根据后缀名判断该文件是不是Word文档
filename = input("请输入带后缀的文件名（如abc.docx）：")

# endswith方法 string.endswith(obj, beg=0, end=len(string))
# 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
if filename.endswith('.doc') or filename.endswith('.docx'):
    print("这是一个Word文档。")
else:
    print("这不是一个Word文档。")
"""