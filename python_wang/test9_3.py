
"""3.编写程序，接收选手的姓名和票数，以end作为结束，输出排序后的成绩"""
score = {}
print("请输入选手的姓名和票数。输入 'end' 结束输入。")
while True:
    name = input("请输入选手的姓名（输入 'end' 结束）：")
    if name.lower() == 'end':
        break
    while True:
        try:
            piao = int(input(f"请输入{name}的票数："))
            if piao < 0:
                print("票数不能为负数，请重新输入。")
                continue
            break
        except ValueError:
            print("票数必须是整数，请重新输入。")
    score[name] = piao
if not score:
    print("没有输入任何选手的成绩。")
else:
    sorted_scores = sorted(score.items(), key=lambda item: item[1], reverse=True)

    print("\n排序后的成绩：")
    for rank, (name, piao) in enumerate(sorted_scores, start=1):
        print(f"{rank}. {name}: {piao}票")
