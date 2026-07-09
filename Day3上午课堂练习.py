import numpy as np

students = []  # [(name, score), ...]

def show_menu():
    print("\n" + "="*28)
    print("      成绩分析系统")
    print("="*28)
    print("1. 输入成绩数据")
    print("2. 查看成绩统计")
    print("3. 查看成绩排名")
    print("4. 查看成绩分布")
    print("5. 查询学生成绩")
    print("6. 退出系统")

def input_scores():
    global students
    n = int(input("请输入学生人数: "))
    students = []
    for i in range(1, n+1):
        name = input(f"第{i}个学生姓名: ").strip()
        score = float(input("成绩: "))
        students.append((name, score))
    print(f"已录入{n}名学生成绩。")

def show_stats():
    if not students: print("请先录入成绩！"); return
    scores = np.array([s[1] for s in students])
    print(f"平均分: {np.mean(scores):.2f}")
    print(f"最高分: {np.max(scores):.2f}")
    print(f"最低分: {np.min(scores):.2f}")
    print(f"标准差: {np.std(scores, ddof=1):.2f}")
    print(f"及格率(≥60): {np.mean(scores >= 60) * 100:.1f}%")

def show_ranking():
    if not students: print("请先录入成绩！"); return
    ranked = sorted(students, key=lambda x: x[1], reverse=True)
    print("排名  姓名  成绩")
    for i, (name, score) in enumerate(ranked, 1):
        print(f"{i:3d}  {name:4s}  {score:5.1f}")

def show_distribution():
    if not students: print("请先录入成绩！"); return
    scores = np.array([s[1] for s in students])
    bins = [0, 60, 70, 80, 90, 100]
    labels = ["不及格(0-59)", "及格(60-69)", "中等(70-79)", "良好(80-89)", "优秀(90-100)"]
    counts, _ = np.histogram(scores, bins=bins)
    print("等级分布：")
    for lab, cnt in zip(labels, counts):
        print(f"  {lab}: {cnt}人")

def query_student():
    if not students: print("请先录入成绩！"); return
    name = input("请输入查询姓名: ").strip()
    found = [s for s in students if s[0] == name]
    if found:
        for n, sc in found:
            print(f"{n} 的成绩: {sc}")
    else:
        print("未找到该学生。")

def main():
    while True:
        show_menu()
        choice = input("请选择: ").strip()
        if choice == '1': input_scores()
        elif choice == '2': show_stats()
        elif choice == '3': show_ranking()
        elif choice == '4': show_distribution()
        elif choice == '5': query_student()
        elif choice == '6': print("再见！"); break
        else: print("无效选项，请重试。")

if __name__ == "__main__":
    main()