# Split operation is used here
message = input("> ")
words = message.split(" ")
emojis = {
    ":)" : "😉" , # win + semicolon or fullstop
    ":(" : "😒",
    "<3" : "❤"  
}
output = "Result: "
for word in words:
    output += emojis.get(word, word) + " "
print(output)
 
message = input("> ")
print(message.split()) 
# output = ['hi', 'bibek', 'how', 'are', 'you']