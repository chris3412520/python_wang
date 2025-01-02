
"""输出2000年以来所有的闰年。"""


for year in range(2000,2025):
    if (year%4==0 and year%100!=0)or(year%400==0):
        print(year)