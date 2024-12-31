"""assert语句又称为“断言”语句，当表达式为假时，程序会抛出异常，其语法格式如下所示：
assert 表达式[,  异常信息]
"""
num_one = int(input("请输入被除数："))
num_two = int(input("请输入除数："))
assert num_two != 0, '除数不能为0'  # assert语句判定num_two不等于0
result = num_one / num_two
print(num_one, '/', num_two, '=', result)
"""8.3.3 异常的传递
如果程序中的异常没有被处理，默认情况下会将该异常传递到上一级，如果上一级仍然没有处理异常，那么会继续向上传递，直至异常被处理或程序崩溃。
"""
"""19周
1月2号
55开 测试 实验
卷面分50分以上"""