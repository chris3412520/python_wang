"""5.输入10个学生考试成绩存入列表，输出所有成绩，输出最高分、最低分和平均分。"""
def students_score():
    scores = []
    # 假设我们要读10个整数
    print("请输入10个学生成绩：")
    for i in range(10):
        score = float(input(f"第 {i+1} 个成绩: "))
        scores.append(score)

    print("所有成绩:", scores)
    max_score = max(scores)
    min_score = min(scores)
    avg_score = sum(scores) / len(scores)

    print(f"最高分: {max_score}")
    print(f"最低分: {min_score}")
    print(f"平均分: {avg_score:.2f}")

students_score()