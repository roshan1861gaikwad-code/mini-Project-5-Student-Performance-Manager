
students = []


def add_student():
    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()

    if not name or not roll_no:
        print("Name and roll number cannot be empty.")
        return

    for student in students:
        if student["roll_no"] == roll_no:
            print("This roll number already exists!")
            return

    try:
        marks = float(input("Enter marks (0-100): "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter valid numeric marks.")
        return

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- STUDENT RECORDS ---")

    for student in students:
        print("Name:", student["name"])
        print("Roll Number:", student["roll_no"])
        print("Marks:", student["marks"])
        print("-" * 25)


def search_student():
    roll_no = input("Enter roll number to search: ").strip()

    for student in students:
        if student["roll_no"] == roll_no:
            print("Student found!")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_no"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


def update_marks():
    roll_no = input("Enter roll number: ").strip()

    for student in students:
        if student["roll_no"] == roll_no:
            try:
                marks = float(input("Enter new marks (0-100): "))

                if not 0 <= marks <= 100:
                    print("Marks must be between 0 and 100.")
                    return

                student["marks"] = marks
                print("Marks updated successfully!")
                return

            except ValueError:
                print("Please enter valid numeric marks.")
                return

    print("Student not found.")


def delete_student():
    roll_no = input("Enter roll number to delete: ").strip()

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def calculate_average():
    if not students:
        print("No records available to calculate average.")
        return

    total = sum(student["marks"] for student in students)
    average = total / len(students)

    print(f"Class average: {average:.2f}")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Calculate Class Average")
    print("7. Exit")

    choice = input("Choose an option (1-7): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        calculate_average()
    elif choice == "7":
        print("Thank you for using the Student Management System!")
        break
    else:
        print("Invalid choice. Please select 1-7.")
