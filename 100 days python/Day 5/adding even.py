# add even number less than 10
highest_limit = int(input("Enter the highest limit: "))
add_even=0
for n in range(0, highest_limit):
    if n %2 ==0:
        add_even = add_even + n 
print(f"answer is {add_even}")
# 0+2+4+6+8