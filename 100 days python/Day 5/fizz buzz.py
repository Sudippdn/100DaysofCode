integers = int(input("Enter an integer: "))
for number in range(1,integers):
    if number%3 == 0:
        if number %5 == 0:
            print("fizzbuzz")
        else:
            print("Fizz")
    elif number %5 == 0:
        print("buzz")
    else:
        print(number)
    
    