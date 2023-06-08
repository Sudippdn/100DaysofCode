# user defined input and print the sum of the digits of the two digit number
# 1. General way
number = int(input("Enter the two digit numebr "))
tens = number /10
ones = number % 10
print("The sum of ones and tens opsition is " + f"{int(tens) + ones}")

# 2. Using the feature of python
number = input("Enter the two digit numebr ")
first_digit = number[0]
second_digit = number[1]
print(first_digit)
print(second_digit)
print(int(first_digit)+int(second_digit))
