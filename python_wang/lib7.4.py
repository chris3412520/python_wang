"""将“hello world hello python” 变成 “python hello world hello ”倒序结构输出。"""

line=input("line:")
l=line.split(" ")

new_l=" ".join(l[::-1])
print(new_l)

"""def reverse_sentence():
    s = "hello world hello python"
    words = s.split()                # ["hello", "world", "hello", "python"]
    words_reversed = words[::-1]     # ["python", "hello", "world", "hello"]
    new_s = " ".join(words_reversed)
    print(new_s)
reverse_sentence()"""