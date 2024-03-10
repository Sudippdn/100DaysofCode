# TABLE OF CONTENTS
project along with date will be here  
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
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print("The sum of a and b is " + f"{a+b}")
```
### "While True:" 
we can declare input multiple times and check answer by declaring "while true"
```python
while True:
    age = int(input("Enter age of the candidate"))
    print(age)
    
    # all the input repeate
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
### Nested Dictionary
Using dictionary inside the main dictionary
```python
Coffee ={
    "Espresso" : {
        "CoffeeAmt" : '18g',
        "WaterAmt" : "50 ml",
        "Price" : "$1.5"
    },
    "Latte" : {
        "WaterAmt" : "200ml",
        "CoffeeAmt" : "24g",
        "Milk" : "150ml",
        "Price" : "$2.5"
    },
    "Cappaccino" : {
        "waterAmt" : "250ml",
        "CoffeeAmt" : "24g",
        "Milk" : "100ml",
        "Price" : "$3.00"
    }
}
# print statement to print the information of latte form the dictionary
print(Coffee["Latte"])

# here is a way to access the value of item from the dictionary
print(Coffee["Latte"]["Price"])   # Output = $2.5
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
  # Day 10
  ## Rock Paper Scissor
  It was interesting playing with the codes. Today, I created a rock, paper, scissor game using python. I got to introduced with pythoon module random. I was introduced with "import random" which takes list of data but functions need to be executed likely. I got to know about random function, random.randint(), random.choose(), etc.

  #### Code for rock paper scissor game
  ```python
while True:
    import random
    options = (
        '''
            __________   
        ---'    ______)______
                    _________)__
                ________________)
                (______)
        ---.____(______)
        ''',
        '''
            ____________   
        ---'    (_______)
                (_______)
                (_______)
                (_______)
        ---.____(_______)
        ''',
        '''
            ____________   
        ---'    ________)____
                    _________)_
                    ___________)
                _____________)
        ---.________________)
        '''
    )
    scissor, rock, paper = options
    make_a_choice = input("Make a choice: ")
    while make_a_choice == "rock":
        make_a_choice = rock
        print(make_a_choice)
        break
        
    while make_a_choice == "paper":
        make_a_choice = paper
        print(make_a_choice)
        break
    while make_a_choice == "scissor":
        make_a_choice = scissor
        print(make_a_choice)
        break
    # while make_a_choice is not options:
    #     print("Invalid inputs")
    #     break
    print("Computer will chooose")
    random_selection = random.choice([rock,paper,scissor])
    print(random_selection)
    if make_a_choice == rock and random_selection == paper or make_a_choice == paper and random_selection == scissor or make_a_choice == scissor and random_selection == rock:
         print("You lose")
    elif make_a_choice == random_selection:
        print("It's a tie!")
    else:
        print("Congratulations! You won")
  ```
# Day 11
## Generate a password
Here is a simple project to generate a random password according to the user defined number of letters, symbols and numbers.
In this project, I was intorduced with the random module that could shuffle and choice for choosing the random character from the given list. I also learned here to convert the given variable into list. The  overall project was pretty simple but lagging with the application of the simple functions were challenging.

#### Here are few import random module functions
##### Shuffle()
```python
import random
random.shuffle(*)
# * inside parenthesis represents the list of items to shuffle 
```
##### Choice()
```python
import random
random.choice(*)
# * inside parenthesis represents the list of items(characters) to choose randomlt
```
#### Code to generate random password
 ```python
import random
letters = ['a','b','c','d','e','e','f','f','g','h','h','i','j','k',
          'l','m','n','o','p','q','r','s','t','u','v','w',
          'x','y','z','A','B','C','E','F','G','H','I','J',
          'K','L','M','N','O','P','Q','R','S','T','U','V',
          'W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','+','-','<','>','/','{','}']

print("-----Generate a random password-----\n")
password = int(input("Enter the number of characters in password: "))
ps_letter = int(input("Enter the number of letters you want: "))
ps_symbol = int(input("Enter the number of symbols you want: "))
ps_numbers = int(input("Enter the number of numbers you want: "))

password_list = []
for char in range(0, ps_letter):
    password_list.append(random.choice(letters))
for char in range(0, ps_symbol):
    password_list += random.choice(symbols)
for char in range(0,ps_numbers):
    password_list += random.choice(numbers)
    
print(password_list)     #Here is list of password without shuffle    
random.shuffle(password_list)
print(password_list)       #Here is list of password after shuffle

password = ""
for char in password_list:
    password += char 
print(f"Your password is {password}")
 ```
# Day 12
## Caesar Cipher
Here is a program to generate ta caesar cipher which enable to transfer a message which need to decode before knowing the actual encrypted message 
```python
# listed alphabets 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# caesar function
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
      if char in alphabet:
          position = alphabet.index(char)
          new_position = position + shift_amount
          end_text += alphabet[new_position]
      else:
        end_text = end_text + char
            
  # To print the logo
  print(f"Here's the {cipher_direction}d result: {end_text}")
  from art import logo

# loop to to type if you want to quit or continue
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Type 'yes' if you want to go, otherwise type 'no': ")
    if result == "no":
        should_end = True
        print("program halted! ")

```
# Day 13
Guessing number along with difficulty level
```python
from random import randint

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5

# function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of numberes remaining"""
    if guess > answer:
        print("Too high!")
        return turns -1
    elif guess < answer:
        print("Too low")
        return turns -1
    else:
        print(f"You got it right asnwer {answer}")

# make a function to set difficulty
def set_difficulty():
    level = input("Chhose 'easy' or 'hard' difficulty: ")
    if level == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN

def game():
    # choosing a number by computer
    print("Welcome to the guessing game")
    print("I am thinking a number between 1 and 100")
    answer = randint(1,100)
    print(f"The correct answer is:{answer}")
    
    turns = set_difficulty()
    
    # Repeat the guessing functionlity if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attemps remaining to guess a number")
       
        # let the user guess the  
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You run out of guesses, you lose")
            exit(0)

game()
```
# Day 14
Here is a day to play around the code and I found this super easy but interesting thing with me to build a qr code using python. It made me realize that I hadn't introduced path of a python file in environment variable. I then installed qrcode module using:
```python
pip install qrcode
```
which is super easy task for me.
```python
import os
import qrcode

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    file_path = os.path.abspath(file_name)
    img.save(file_path)

# Example usage
data = """github.com/Sudippdn
linkedin.com/in/sudip-pradhan-a0a804239/

Hi, it's me Sudip! This is a first qr code generate using python
"""
file_name = "C:/Users/Sudip/Desktop/qrcode.png"
generate_qr_code(data, file_name)
```
### You can connect me through
![qrcode](https://github.com/Sudippdn/100DaysofCode/assets/104957400/83474155-bee1-4900-8621-8b8f88f03240)

# Day 15
## Coffee Machine
I have divided a program in two files and import the data from "items.py" to '"coffee machine.py"

#### Here is items.py part program
In this part, I constructed MENU file for the coffee items along with the ingredients required. The cost of the particular types of coffee is also mentioned here.
```python
MENU = {
    "Espresso": {
        "ingredients": {
            "Coffee": 18,
            "Water": 50,
        },
        "Cost": 1.5
    },
    "Latte": {
        "ingredients": {
            "Water": 200,
            "Coffee": 24,
            "Milk": 150
        },
        "Cost": 2.5
    },
    "Cappuccino": {
        "ingredients": {
            "Water": 250,
            "Coffee": 24,
            "Milk": 100
        },
        "Cost": 3.0,
    }
}

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100
}
```
#### Here is a programming code for "coffee machine.py"
In this part of the program, I have imported MENU and resources from items which is located in items.py. Created different functions for the operations and perform the differtent task. In these program, the machine checks the inserted coin total value and perform it its is sufficient or not along with the refund amount if it exceed.
```python
from items import MENU
from items import resources
profit = 0


def is_resource_sufficient(order_ingredients):
    """Returns True when orders can be made and False when ingredients is insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coin():
    """Returns the total calculated from coins inserted"""
    total = 0
    print("Please insert coin!")
    total += int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickels? ")) * 0.01
    total += int(input("How many penny? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded!!!")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the reqyired ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is you {drink_name}🤞")


is_on = True
while is_on:
    choice = input("What would you like? (Espresso/Latte/Cappuccino): ")
    if choice == "exit":
        is_on = False
    elif choice == "reports":
        print(f"Water = {resources['Water']}ml")
        print(f"Milk = {resources['Milk']}ml")
        print(f"Coffee = {resources['Coffee']}gram")
        print(f"Money = ${profit} \n")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["Cost"]):
                make_coffee(choice, drink["ingredients"])
```
# Testing
