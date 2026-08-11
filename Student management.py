students = {}


def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    students[roll] = {
        "name": name,
        "course": course,
        "marks": marks
    }

    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\n----- Student Records -----")

    for roll, data in students.items():
        print(f"Roll No : {roll}")
        print(f"Name    : {data['name']}")
        print(f"Course  : {data['course']}")
        print(f"Marks   : {data['marks']}")
        print("---------------------------")


def search_student():
    roll = input("Enter Roll Number to search: ")

    if roll in students:
        data = students[roll]

        print("\nStudent Found!")
        print(f"Roll No : {roll}")
        print(f"Name    : {data['name']}")
        print(f"Course  : {data['course']}")
        print(f"Marks   : {data['marks']}")
    else:
        print("Student not found.")


def delete_student():
    roll = input("Enter Roll Number to delete: ")

    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found.")


while True:
    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Program exited.")
        break

    else:
        print("Invalid choice!")
