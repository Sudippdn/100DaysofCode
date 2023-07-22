import random
print("Welcome to the number game!")
print("I am thining a number between 1 to 100")

# creating a list using range and append
list = []
number = 0
for num in range(1, 101):
    list.append(num)    
print(f"Numbers in list are:  {list}")
RandNum = random.choice(list)
print(f"Random number is {RandNum}")

# function to call easy one
def choice(easy):
    chances = 10
    count = 0
    if chances > count:
        chances -= 1
        count += 1
        guess = int(input(f"Make a guess for easy: "))
    if guess < RandNum:
        if guess * 2 > RandNum:
            print("Your guess is low")
            choice("hard")
        else:
            print("Your guess is too low")
            choice("hard")
    elif guess > RandNum:
        if guess / 2 < RandNum:
            print("Your guess is high")
            choice("hard")
        else:
            print("Your guess is too high")
            choice("hard")
    elif guess == RandNum:
        print("Congratulation!!! You made a correct guess")
    exit       

# function to call hard level
def choice(hard):
    chances = 5
    count = 0
    if chances > count:
        chances -= 1
        count += 1
        guess = int(input(f"Make a guess:"))
        if guess < RandNum:
            if guess * 2 > RandNum:
                print("Your guess is low")
                choice("hard")
            else:
                print("Your guess is too low")
                choice("hard")
        elif guess > RandNum:
            if guess / 2 < RandNum:
                print("Your guess is high")
                choice("hard")
            else:
                print("Your guess is too high")
                choice("hard")
        elif guess == RandNum:
            print("Congratulation!!! You made a correct guess")
        exit()

# difficulty selection       
difficulty = input("Type 'easy' or 'hard': ")
if difficulty == "easy":
    choice('easy')
elif difficulty == "hard":
    choice('hard')     
