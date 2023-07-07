from replit import clear # clear  need to be imported to run this code somehow
#HINT: You can call clear() to clear the output in the console.
biding = {}
biding_finish = False
def finding_highest_bid(biding_records):
  bid_amount = 0
  highest_bid = 0  
  winner = ""
  for bidder in biding_records:
    bid_amount = biding_records[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"Winner is {winner} with the ${highest_bid}")

while not biding_finish:
    name = input("Enter your name: ")
    price = int(input("Enter you bid: $"))
    biding[name] = price
    should_countinue = input("Enter 'yes' if you want to continue, else enter 'No': ")
    if should_countinue == "No":
        biding_finish = True
        finding_highest_bid(biding)
    elif should_countinue == "yes":
        clear()    
    