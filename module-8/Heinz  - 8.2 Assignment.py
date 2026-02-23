import json


def print_students(students):
    for s in students:
        print(f"{s['L_Name']}, {s['F_Name']} : ID = {s['Student_ID']} , Email = {s['Email']}")


# Load the JSON file
with open("student.json", "r") as file:
    students = json.load(file)

# Print original list
print("This is the original Student list:\n")
print_students(students)

# Add new student
new_student = {
    "F_Name": "Brady",
    "L_Name": "Heinz",
    "Student_ID": 1212,
    "Email": "bheinz@hotmail.com"
}

students.append(new_student)

# Print updated list
print("\nThis is the updated Student list:\n")
print_students(students)

# Write updated list back to file
with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nThe student.json file was updated.")