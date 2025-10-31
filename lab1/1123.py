groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [2, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 3, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
print_students(groupmates)


def filter_students_by_average(students, min_average):
    filtered_students = []
    for student in students:
        average_mark = sum(student["marks"]) / len(student["marks"])
        if average_mark > min_average:
            filtered_students.append(student)
    return filtered_students

min_average = float(input("Введите минимальный средний балл для фильтрации: "))

filtered_students = filter_students_by_average(groupmates, min_average)
if filtered_students:
 print(f"\nСтуденты со средним баллом выше {min_average}:")
print_students(filtered_students)
