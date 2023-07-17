card_value = [11,2,3,4,5,6,7,8,9,10,10,10,10]
import random
results = ""
choice = ""

for items in card_value:
    rand1 = int(random.choice(card_value))
    rand2 = int(random.choice(card_value))
    rand3 = int(random.choice(card_value))
    break
addRand = rand1 + rand2
print(f"Your cards: [{rand1}, {rand2}], current score = {addRand}")
print(f"Computer's first card: {rand3}")
if addRand ==21:
    print("Congratulation!!! You won the match")
    break
get_anotherCard = True
while get_anotherCard:
    choice = input("Do you want another card? (y/n): ")
    while addRand <=21:
        if choice == 'y':
            if addRand < 17:
                card_value[0] = 1
            newRand = random.choice(card_value)
            newAdd = addRand + newRand
            print(f"Your final card: [{rand1}, {rand2}, {newRand}], final score = {newAdd}")
            break
        elif choice == 'n':
            get_anotherCard = False
    if newAdd >21:
        print("Sadly you exceeded 21, You lost!!!")
        get_anotherCard = False
    elif (newAdd == 21):
        print("Congratulations, You won!!!")
    else:
        rand4 = random.choice(card_value)
        rand5 = random.choice(card_value)
        CompAdd = int(rand4) + int(rand5) + rand3
        print(f"Computer final cards: [{rand4}, {rand5}], Computer score = {CompAdd}")
    
        if (newAdd == CompAdd):
            print("Game is Draw!!!")
        elif (newAdd < CompAdd and CompAdd < 21):
            print("Computer wins")
        elif (newAdd > CompAdd):
            print("Congratulation, you won")
    break
        
