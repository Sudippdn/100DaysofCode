def No_of_Can(height, width, cover):
    no_of_items = (height*width)/cover
    print(f"No of can is {round(no_of_items,0)}")
   

test_h = int(input("Enter the height of wall: "))
test_w = int(input("Enter the width of wall: "))
coverage = 5
No_of_Can(height = test_h, width = test_w, cover = coverage)



