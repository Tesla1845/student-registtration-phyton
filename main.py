students = []

def register_student():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["ID"] == student_id:
            print("Error: Student ID already exists!")
            return

    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    department = input("Enter Department: ")

    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Department": department
    }

    students.append(student)

    print("Student registered successfully!")

def view_students():
    if not students:
        print("No students registered yet.")
        return

    print("\n===== REGISTERED STUDENTS =====")

    for student in students:
        print("------------------------------")
        print("Student ID:", student["ID"])
        print("Name:", student["Name"])
        print("Age:", student["Age"])
        print("Department:", student["Department"])

    print("------------------------------")

def search_student():
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["ID"] == student_id:
            print("\n===== STUDENT FOUND =====")
            print("Student ID:", student["ID"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Department:", student["Department"])
            return

    print("Student not found!")

def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["ID"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found!")

def update_student():
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["ID"] == student_id:
            print("\nEnter new student information:")

            name = input("Enter new name: ")
            age = input("Enter new age: ")
            department = input("Enter new department: ")

            student["Name"] = name
            student["Age"] = age
            student["Department"] = department

            print("Student updated successfully!")
            return

    print("Student not found!")

while True:
    print("\n================================")
    print("   STUDENT REGISTRATION SYSTEM")
    print("================================")
    print("1. Register Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Please enter 1-6.")
