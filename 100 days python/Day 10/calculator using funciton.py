def add(n1, n2):
    return n1+n2
def sub(n1, n2):
    return n1-n2
def mul(n1, n2):
    return n1*n2
def div(n1, n2):
    return n1/n2
# def add(n1, n2):
#     return n1+n2
choice = ""
# result = ""
n1 = int(input("Enter a first number: "))
n2 = int(input("Enter a second number: "))
# print('''Here're the operation you can perform:
#       +
#       -
#       /
#       *''')
# choice = input("make a choice: ")
# n2 = int(input("Enter a second number: "))

# if choice == "+":
#     result = add(n1,n2)
# elif choice == "=":
#     result = sub(n1,n2)
# elif choice == "*":
#     result = mul(n1,n2)
# elif choice == "/":
#     result = div(n1,n2)
value = {
    "+" : add(n1, n2), # here we can simply give he name of he opetation to call it to the next opetation
    "-" : sub(n1,n2),
    "*" : mul(n1,n2),
    "/" : div(n1,n2)      
}
for key in value:
    print(key)
print(input("Enter the operation to execute: "))
for key in value:
    if choice == key:
        result = value[key]
    result = value[key]   #This code is not finished as we can do it by another way
print(f"The operation of the program is {result}")