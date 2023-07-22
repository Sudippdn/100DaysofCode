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