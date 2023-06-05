command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The car is already started...")
        else:
            started = True
            print("car started....")
    elif command == "stop":
        if not started:
            print("The car is already stopped")
        else:
            started = False
            print("car stopped....")
    elif command == "help":
        print("""
        start = to start the car
        stop = to stop the car
        exit = to halt the program
        help = to provide technical help""")
    elif command == "exit":
        break
else:
    print("The input is invalid")