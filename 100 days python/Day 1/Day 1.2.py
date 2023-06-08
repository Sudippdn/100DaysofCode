print("welcome to the tip calculator")
bill_amount = int(input("What is the total bill? "))
no_of_customers = int(input("How many people to split the bill?  "))
tip_percentage = float(input("What percentage tip are you willing to give? "))
total = 0
total = total + (tip_percentage/100) * bill_amount 
print(f"Each person should pay:-  {total/5}")