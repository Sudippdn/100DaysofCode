# Note: When we take range as an input, the cartesian product always shows from 0
first = int(input("Enter the size of first set"))
second = int(input("Enter the size of second set"))
print("The cartesian product of two sets are")
for x in range(first):
    for y in range(second):
        print(f"({x},{y})")