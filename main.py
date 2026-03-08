import sqlite3

#Підключення до бази даних
connection = sqlite3.connect('university.db')
cursor = connection.cursor()

#Створення таблиці
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    major TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    course_name TEXT,
                    teacher TEXT
                )''')


cursor.execute('''CREATE TABLE IF NOT EXISTS student_courses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER,
                    course_id INTEGER,
                    FOREIGN KEY (student_id) REFERENCES students(id),
                    FOREIGN KEY (course_id) REFERENCES courses(id)
                )''')

#Інтерфейс
while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. 3aреєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")
    if choice == "1":
        # Додавання нового студента
        name = input("Введіть ім'я студента: ")
        age = int(input("Введіть вік студента: "))
        major = input("Введіть спеціальність студента: ")

        cursor.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)", (name, age, major))
        connection.commit()

    elif choice == "2":
        # Додавання нового курсу
        course_name = input("Введіть ім'я студента: ")
        teacher = input("Введіть спеціальність студента: ")

        cursor.execute("INSERT INTO courses (course_name, teacher) VALUES (?, ?)", (course_name, teacher,))
        connection.commit()

    elif choice == "3":
        # Показати список студентів
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()
        if not students:
            print("Немає студентів у базі даних.")
        else:
            print("\nСписок студентів:")
            for student in students:
                print(f"ID: {student[0]}, Ім'я: {student[1]}, Вік: {student[2]}, Спеціальність: {student[3]}")

    elif choice == "4":
        #Показати список курсів
        cursor.execute('SELECT * FROM courses')
        courses = cursor.fetchall()
        if not courses:
            print("Немає курсів у базі даних.")
        else:
            print("\nСписок курсів:")
            for course in courses:
                print(f"ID: {course[0]}, Ім'я: {course[1]}, Вчитель: {course[2]}, ")

    elif choice == "5":
        # Зареєструвати студента на курс
        pass
    elif choice == "6":
        # Показати студентів на конкретному курсі
        pass
    elif choice == "7":
        break
    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")