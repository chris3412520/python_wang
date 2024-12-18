"""根据组织数据时与数据有联系的参数的数量，数据可分为一维数据、二维数据和多维数据。

具有对等关系的一组线性数据，如：
一维列表
一维元组
集合

二维数据关联参数的数量为2，如：
矩阵
二维数组
二维列表
二维元组

利用键值对等简单的二元关系展示数据间的复杂结构，如：
字典

1.数据存储
一维数据呈线性排列，一般用特殊字符分隔，例如：
使用空格分隔：成都 杭州 重庆 武汉 苏州 西安 天津
使用逗号分隔：成都,杭州,重庆,武汉,苏州,西安,天津
使用&分隔：成都&杭州&重庆&武汉&苏州&西安&天津
一维数据的存储需要注意以下几点：
同一文件或同组文件一般使用同一分隔符分隔。
分隔数据的分隔符不应出现在数据中。
分隔符为英文半角符号，一般不使用中文符号作为分隔符。

二维数据可视为多条一维数据的集合，当二维数据只有一个元素时，这个二维数据就是一维数据。
CSV（Commae-Separeted Values，逗号分隔值）是国际上通用的一二维数据存储格式。

CSV格式规范：
以纯文本形式存储表格数据
文件的每一行对应表格中的一条数据记录
每条记录由一个或多个字段组成
字段之间使用逗号（英文、半角）分隔

csv文件的广泛应用
数据导入与导出：CSV文件是许多软件和数据库系统的标准数据交换格式。通过将数据导出为CSV文件，用户可以轻松地将数据从一个平台迁移到另一个平台，实现数据的无缝迁移和共享。
数据分析与统计：CSV文件常用于数据分析和统计领域。
数据备份与存档：CSV文件作为一种轻量级的数据存储格式，常用于数据备份和存档。
"""
csv_file = open('score.csv')
lines = []
for line in csv_file:
		line = line.replace('\n','')
		lines.append(line.split(','))
print(lines)
csv_file.close()