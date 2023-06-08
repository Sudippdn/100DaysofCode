height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: ")) 
BMI = weight / (height**2)
print(round(BMI,2))  #round will be use to declare the no of decimal number we expect
