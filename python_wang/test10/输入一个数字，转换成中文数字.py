# =============================================================================
# 作者: 成照权
# 日期: 2024-12-9
# 描述: 输入一个数字，转换成中文数字。比如1234567890->壹贰叁肆伍陆柒捌玖零。
# =============================================================================
dict1 = {
    '0': '零',
    '1': '壹',
    '2': '贰',
    '3': '叁',
    '4': '肆',
    '5': '伍',
    '6': '陆',
    '7': '柒',
    '8': '捌',
    '9': '玖',
}
a=(input("请输入一串数："))
print(type(a))
for i in a:
    print(dict1[i],end="")