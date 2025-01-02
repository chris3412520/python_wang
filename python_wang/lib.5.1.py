

"""输入一行字符，每两个单词之间以空格隔开，统计其中有多少个单词，
如输入：This is a Python program.  输出:There are 5 words in the line """
line_ch=input("ch:")
new_line=line_ch.split(' ')

num=len(new_line)
print(f'There are {num} words in the line')
