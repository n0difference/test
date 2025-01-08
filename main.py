def calculate_average(grades):
    average = 0
    for i in grades:
        average += i
    return (average/len(grades))


def student_info(students):
    for i in students:
        print(f"Студент: {i['name']}",
              f"Средний балл: {calculate_average(i['grades'])}",
              f"Статус: {'Отстающий' if calculate_average(i['grades']) < 75 else 'Успешен'}", sep="\n")


def worst_student(students):
    worst = {"name": "", "grades": [1000]}
    for i in students:
        if calculate_average(i["grades"]) < calculate_average(worst["grades"]):
            worst = i
    return worst


students = [{"name": "Alice", "grades": [90, 95, 100]},
            {"name": "Bill", "grades": [85, 90, 95]},
            {"name": "Carl", "grades": [80, 85, 90]},
            {"name": "Daniel", "grades": [75, 80, 85]},
            {"name": "Egor", "grades": [70, 75, 80]},
            {"name": "Ford", "grades": [65, 70, 75]}]

student_info(students)

students.append({"name": "Rick", "grades": [100, 100, 100]})

student_info(students)

students.remove(worst_student(students))

student_info(students)

