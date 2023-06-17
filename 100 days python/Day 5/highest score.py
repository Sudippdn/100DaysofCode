# calculating highest score form the list taken from user defined
students = input("Enter the marks of students: ").split()
highest_score = 0
for n in range(0, len(students)):
  if (highest_score < int(students[n])):
    highest_score = int(students[n])
    highest_score= int(students[n])
  else:
    print("There is nothing here")
print(f"The highest score is {highest_score}")