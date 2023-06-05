# taking input age mark as an integer
age= int(input("Enter your age: "))
mark = int(input("Enter your marks obtained: "))
# comparing age as an integer with 18
if (age>=18):
    # comparing mark as an integer with 50
    if (mark>=50):
        print("He is eligible for the job")
    else:
        print("He is not eligible for the job!")
else:
    print("He is not eligible for the job!")
   
# checking the largest number in the list using for loop 
numbers = [3,6,2,8,4,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print("\nThe largest number in the list is:")
print(max)