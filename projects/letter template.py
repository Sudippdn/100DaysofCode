# print("\n10. Send letter to multiple people")
letter = '''Hello, <|NAME|>
You have been selected in my python program.
Happy to see you in the program.
Greeeting from the company head.

Date: <|DATE|>'''

name=input("Enter name of the candidate: ")
date=input("Enter date: ")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)