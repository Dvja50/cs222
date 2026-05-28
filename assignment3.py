
def load_students(filename):
    students = {}

    file = open(filename, "r")

    for line in file:
        line = line.strip()

        
        data = line.split(",")

        student_id = data[0]
        last_name = data[1]
        first_name = data[2]
        major = data[3]
        gpa = data[4]

      
        students[student_id] = [last_name, first_name, major, gpa]

    file.close()

    return students



def search_last_name(students):
    search_name = input("Enter last name to search for: ")

    found = False

    for student_id in students:
        info = students[student_id]

        if info[0].lower() == search_name.lower():
            print(student_id, info[0], info[1], info[2], info[3])
            found = True

    if not found:
        print("No students found.")



def search_major(students):
    search_major_name = input("Enter major to search for: ")

    found = False

    for student_id in students:
        info = students[student_id]

        if info[2].lower() == search_major_name.lower():
            print(student_id, info[0], info[1], info[2], info[3])
            found = True

    if not found:
        print("No students found.")



def main():

    students = load_students("students.txt")

    choice = ""

    
    while choice != "3":

        print("\nChoose an option:")
        print("1) Search by Last Name")
        print("2) Search by Major")
        print("3) Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            search_last_name(students)

        elif choice == "2":
            search_major(students)

        elif choice == "3":
            print("Goodbye!")

        else:
            print("Invalid choice.")



main()