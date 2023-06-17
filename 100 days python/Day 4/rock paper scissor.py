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
         print("Sorry! You lose")
    elif make_a_choice == random_selection:
        print("It's tie!")
    else:
        print("Congratulation!You won")
        