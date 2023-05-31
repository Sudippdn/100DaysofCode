# Day 1

Here is how we can declare the variables in python. Python is an easiest programming language in case of data declaration. Data type in python don't need to declare individually instead it identify the type of data we declared automatically.


##  Variable declaration
#### Declaring string
```python
# Declaring Strings
first_name = "Sudip "
last_name = 'Pradhan '
print(first_name + last_name + 'from Kathmandu')
```
#### Declaring integer
```python
age = 21
print(age)`
a, b,c, d=40,30,20,10
print(a+b+c)  # output = 90
```
#### Declaring float
```python
prize_win = 8200.53
print(prize_win)`
```
#### Listing data
```python
a= [2,3,4,5,6,7]
a[1]=34
print(a)
print(a[2])
```
### Declaring Matrix 

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][2]) # way to access the value of indivisual element of particular positiion

print("""          
for rows in matrix:          
List of the items are: 
      """)  # tO display the items in matrix
    for items in rows:
        print(items)
```
# Day 2 
## Tuples

Tuples are sequences of elements that can contain different data types that can be defined using either parentheses or not but the output always comes with parentheses.
##### Note
```python
You cann't rewrite or change the value of the element inside the parenthesis of tuples like  listing
```

### Declaring tuples

```python
number1 = 1,2,3 # without using parentheses
number2 = (5,6,7) # using parentheses
print(number1) 
print(number2)
```
#### Output
![tuples](https://github.com/Sudippdn/Python-from-beginning/assets/104957400/0a44ea3a-3272-4259-870a-ad245e374eee)

## Unpacking

Unpacking is the part of tuple that can access the individual elements of tuples. It is a feature of python that can make coding faster and easier.

### Coding part

```python
coordinates = (1,2,3)

# x= coordinates[0]
# y = coordinates[1]
# z= coordinates[2]

# To write the same things of above expressions, we can assign like this; 
x, y, z = coordinates
print(y*z) # Output = 6

```
# Day 3
## Conditional statement 
In python, conditional statement is same like in C or C++ but curly bracket is replaced by colon ':' and 'else if' is replaced  with 'elif'.

### if condition
```
temperature = int(input("Enter tem in degree celcius: "))
if (temperature<30):
    if (temperature>15):
        print("It's bearutiful day")
    else:
        print("It's a cold day")
else:
    print("It's a cold day")
        
```
 Day 4
## Skip Function

### if condition
```
print(variable_name[starting:end:step_skip])
```
```
#slice operator as string
name= "SudipIsGoodBoy"
print(name[0:5]) #Output = Sudip
print(name[0: :3]) # Output=Sisoo

#slice operator as list
list = [2,0,2,3,0,5,2,3]
print(list[2::2]) #Output = [2,0,2]
        
```

