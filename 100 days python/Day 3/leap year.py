# 1. Method first
while True:    # gives continuous input option
    year = int(input("Enter a year:"))
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            print(f"{year} is the leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is not a leap year")

# 2. Alternative method(when above is not commented, while loop won't eccess this one)
while True:  
    year = int(input("Enter the year : "))
    if year % 4 == 0:
        if year % 100 ==0:
            if year % 400 ==0:    
                print(f"{year} is the leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
            
    else:
        print(f"{year} is not a leap year")
