Secret_number= 9
guess_limit= 3
guess_count=0
while guess_count<guess_limit:
    Guess= int(input("Guess: "))
    guess_count+=1
    if Guess==Secret_number:
        print("Congratz! You've made correct guess.")
        break
    else:
        while guess_count==1:
            print("Wrong guess. Now you have 2 chances left")
            break
        while guess_count==2:
            print(" Again wrong guess. Now you have 1 chance left")
            break
else:
    print("You failed")