# # Making a car game using basing if else statements
# car_state= input("> ")
# while car_state=="Start":
#     if car_state=="Started":
#         print("Car started")
#     else:
#         print("Car already started")
#     break
# while car_state=="Stop":
#         if car_state=="Stopped":
#             print("Car stopped")
#         else: 
#             print("Car is already stopped")
#         break








# car_state= input("> ")
state_limit= 1000
state_count= 0
while state_count<state_limit:
    car_state= input("> ")
    if car_state=="Start":
        if car_state=="Stopped":
            # print("car started")
        # else:
            print("Car started")
    elif car_state=="Stop":
        print("Car is stopped")
    elif car_state=="Started":
        print("Car is already stopped")
    elif:
    
