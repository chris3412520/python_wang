
"""输入字符串2021-12-01，转换日期表示形式，输出2021/12/01。（注:分别用replace方法和split+join方法实现）"""
t=input("format(xxxx-xx-xx):")
new_t=t.replace('-','/')
print(new_t)
parts=t.split('-')
new_date='/'.join(parts)
print(new_date)


"""def convert_date_with_split_join():
    date_str = input("请输入日期(格式为YYYY-MM-DD)：")
    parts = date_str.split("-")  # ['2021', '12', '01']
    new_date = "/".join(parts)  # '2021/12/01'
    print(new_date)"""