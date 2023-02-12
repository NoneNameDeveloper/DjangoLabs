from typing import List


groupmates = [
    {
        "name": "Олег",
        "surname": "Нечаев",
        "exams": ["Информатика", "ВВиТ", "Web"],
        "marks": [1, 2, 3]
    },
    {
        "name": "Юрий",
        "surname": "Дружинин",
        "exams": ["Информатика", "ВВиТ", "Web"],
        "marks": [1000, 20000, 3000]
    },
    {
        "name": "Максим",
        "surname": "Марцинкевич",
        "exams": ["Информатика", "ВВиТ", "Web"],
        "marks": [0, 2, 5]
    }, 
    { 
        "name": "Юрий",
        "surname": "Макарченков",
        "exams": ["Информатика", "ВВиТ", "Web"],
        "marks": [10, 20, 30]
    },
    {
        "name": "Кирилл",
        "surname": "Михайлов",
        "exams": ["Информатика", "ВВиТ", "Web"],
        "marks": [100, 200, 300]
    }
]


def filter_students(students: List[dict], average_mark: int = 100) -> None:
    """
    фильтр студентов, со средним баллом выше заданного
    """
    filtered_students = [student for student in students if sum(student["marks"])/len(student["marks"]) > average_mark]  # создаем новый фильтрованный список

    print("Имя".ljust(15), "Фамилия".ljust(10), "Экзамены".ljust(30), "Оценки".ljust(20))  # выводим заголовок нашей "таблицы"

    # вывод информации о прошедших фильтрацию студентах
    for u in filtered_students:
        print(
                u["name"].ljust(15),
                u["surname"].ljust(10),
                ", ".join(u["exams"]).ljust(30),
                ", ".join(str(val) for val in u["marks"]).ljust(20)
            )

average_mark = int(input("Введите средний балл для фильтрации: "))
filter_students(groupmates, average_mark=average_mark)

