students = input("Enter the height of students: ").split()
total_height = 0
for student in students:
    total_height += int(student)
    average_height = int(total_height/len(students))
print(average_height)
     