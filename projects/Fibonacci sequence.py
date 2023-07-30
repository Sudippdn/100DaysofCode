def fibb(n):
    if (n == 0 or n == 1):
        return n
    else:
        return fibb(n-1) + fibb(n-2)

fibbonacci = []
n = int(input("Enter a number: "))
print(f"Fibb sequence of {n} is: ")
for i in range(0, n):
    fibbonacci.append(fibb(i))
print(fibbonacci)
