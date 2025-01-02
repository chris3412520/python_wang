
"""4.根据输入的年份和月份，计算并输出当月的天数。"""
year=int(input("year:"))
month=int(input("month:"))
if month<1 or month>12:
    print("error")
else:
    is_leap=(year%4==0 and year%100!=0) or (year%400==0)
    day_of_month=[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap and month==2:
        print(29)
    else:
        print(f'{year}年{month}月天数为：',day_of_month[month-1])













"""def days_in_month():
    year = int(input("请输入年份："))
    month = int(input("请输入月份（1-12）："))

    # 判断输入合法性
    if month < 1 or month > 12:
        print("输入的月份不正确")
        return

    # 判断闰年
    # 条件： (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    # 各月份天数：这里给出常规情况
    days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 如果是 2 月，且闰年，则加 1 天
    if month == 2 and is_leap:
        print(f"{year} 年 {month} 月有 29 天")
    else:
        print(f"{year} 年 {month} 月有 {days_of_month[month - 1]} 天")


# 测试
# days_in_month()"""