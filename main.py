def calculate_average(grades):
    if grades:
        average = 0
        for i in grades:
            average += i
        return (average/len(grades))
    else:
        print("нет оценок")
        return 0


def student_info(students):
    for student in students:
        average = calculate_average(student['grades'])
        student_status = 'Отстающий' if average < 75 else 'Успешен'
        print(f"Студент: {student['name']}",
              f"Средний балл: {average}",
              f"Статус: {student_status}", sep="\n")


def worst_student(students):
    if students:
        worst = {"name": "", "grades": [1000]}
        for i in students:
            if calculate_average(i["grades"]) < calculate_average(worst["grades"]):
                worst = i
        return worst
    else:
        print("нет студентов")


def average_of_averages(students):
    if students:
        counter = 0
        for student in students:
            counter += calculate_average(student['grades'])
        return (counter/len(students))
    else:
        print("нет студентов")


students = [{"name": "Alice", "grades": [90, 95, 100]},
            {"name": "Bill", "grades": [85, 90, 95]},
            {"name": "Carl", "grades": [80, 85, 90]},
            {"name": "Daniel", "grades": [75, 80, 85]},
            {"name": "Egor", "grades": [70, 75, 80]},
            {"name": "Ford", "grades": [65, 70, 75]}]

student_info(students)

students.append({"name": "Rick", "grades": [100, 100, 100]})

student_info(students)

if worst_student(students):
    students.remove(worst_student(students))
else:
    print("нет студентов для отчисления")

student_info(students)

print(f"Средний балл по всем студентам: {average_of_averages(students)}")