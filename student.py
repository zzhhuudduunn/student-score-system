def show_student():
    name = input("请输入学生姓名：")
    student_id = input("请输入学生学号：")
    score = float(input("请输入学生成绩："))

    print(f"学生姓名：{name}")
    print(f"学生学号：{student_id}")
    print(f"学生成绩：{score}")


if __name__ == "__main__":
    show_student()