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
# way to access the value of indivisual element of particular positiion
print(matrix[0][2]) 

# tO display the items in matrix
print("""          
for rows in matrix:          
List of the items are: 
      """)  
    for items in rows:
        print(items)
```
### Displaying the datatype in python
```python
a=90
b=82.9898984342
b=False
print(type(a)) # output=<class 'int'>
print(type(b)) # output=<class 'float'>
print(type(c)) # output=<class 'bool'>
```
### f string
f string is used to declare to concantited the string and an integer in a same line
```python
a = int(input("Enter the value of a: ))
b = int(input("Enter the value of b: ))
print("The sum of a and b is " + f"{a+b)")

```
# Day 2 
## Tuples

Tuples are sequences of elements that can contain different data types that can be defined using either parentheses or not but the output always comes with parentheses.
##### Note
```word
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
```python
temperature = int(input("Enter tem in degree celcius: "))
if (temperature<30):
    if (temperature>15):
        print("It's bearutiful day")
    else:
        print("It's a cold day")
else:
    print("It's a cold day")
        
```
# Day 4
## Slice Operator

```python
print(variable_name[starting:end:step_skip])
```
#### using slice operator during string 
```python
name= "SudipIsGoodBoy"
print(name[0:5]) #Output = Sudip
print(name[0: :3]) # Output=Sisoo
```
#### Using slice operator during listing
```python
list = [2,0,2,3,0,5,2,3]
print(list[2::2]) #Output = [2,0,2]
        
```
# Day 5
## Dictionary 

Dictionary is a built-in data structure that allows you to store and retrieve data using key-value pairs. Dictionaries are mutable, unordered collections, and they are also known as associative arrays or hash maps in other programming languages.

## Example
#### Constructing dictionary with variable name customers_detail
```python
customers_detail = {
    "Name" : "Sudip Pradhan",
    "age": 21,
    "living" : "Kathmandu"
}
```

#### Accessing and Modifying value by key

```python
print("Before changing name, " + customers_detail["Name"])  # Output =Before changing name, Sudip Pradhan
customers_detail["Name"] = "Rajesh Hamal"                   # modifying value
print("After changing name, " + customers_detail["Name"])   # Output = After changing name, Rajesh Hamal
```
#### Adding new key-value pair
```python
customers_detail["College_Name"]  = "Madan Bhandari Memorial College"
print(customers_detail["College_Name"])         # Output = Madan Bhandari Memorial College
```

#### Removing key-value
```python
del customers_detail["living"]
print(customers_detail.get("living"))           # Output = None
```
#### Displaying the interger value corresponding to their name
```python
hone = input("Phone: ")
numbering = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}
output = ""
for ch in phone:
    output += numbering.get(ch) + " "     # input = 529
print(output )                            # Output = five two nine
```
# Day 6
## Split() method
Split method is used in python to split in a list to the given string to varius substrings
```python
message = "hi bibek how are you"
print(message.split()) 
# output = ['hi', 'bibek', 'how', 'are', 'you']
```
#### Example
Here an exmaple of using split() method to split the given string along with the emoji convertor using dictionary in python
```python
message = input("> ")
words = message.split(" ")
emojis = {
    ":)" : "😉" , # win + semicolon or fullstop
    ":(" : "😒",
    "<3" : "❤"
}
output = " "   # Double inverted commas declares anything before displaying ouptut  
for word in words:
    output += emojis.get(word,  word) + " "
print(output)
 ```
 # Day 7
 ## Function
 Today I learned about the basic uses of funtion in python. In python, we define function by initilizing 'def' keyword. The other parameters are the same like C or C++. The new thing I learned here is, in the calling function, we can pass the argument in two ways, i.e using positional argument and key argument
 
 ### Examples
 #### Function that doesn't return 
  ```python
  def user_name(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
# using both keyword arguments
user_name(last_name ="Pradhan", first_name = "Sudip")
# using both positional arguments
user_name("Sudip","Pradhan")
# using positional and keyword argument
user_name("Sudip", last_name = "Pradhan")

# but we can't mention like
# user_name("first_name = "Sudip", "Pradhan")
# or user_name("Sudip", first_name) as it gives error saying having multiple value of first_name
  ```
  #### Function that return value
 ```python
# Return Value in python
def square(number):
    return number*number
print(square(3))
 ```
 # Day 8
 ## Class
 A class encapsulates data (in the form of attributes or properties) and behaviors (in the form of methods or functions) related to a specific concept or entity. It makes easier for programmer to declare data once and perform for multiple datas using different objects.
 
  ```python
  class A:
    def sum(self):
        print("just kidding")
    def joke(self):
        print("sorry, the joke is done")
a = A() # decalring oject
a.joke() # using class to access funtion
a.x=20
a.sum()
print(a.x)  
   ```
 ### Constructor
 There are two types of constructor in python unlike cpp. They are:
 ```bash
  1. __init__()
  2. __new__()
 ```
 #### 1. __init__()
 ```python
 class first_class:
    def __init__(self, x, y): 
        self.add = x+y
fc = first_class(10, 30)  
print("The sum of x and y is ", fc.add)         # output = 40
```
# Day 9
## Exception
Exception is used to replace the particular type of error in python. Here are the few examples of excemption used instead of ValueError, zeroDivisionError. This helps programmer to understand the particular type of error in the program. 
```python
try:
    age = int(input("age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError: 
    print("Invalid value")
except ZeroDivisionError:
    print("Age cann't be zero")
  ```
  

