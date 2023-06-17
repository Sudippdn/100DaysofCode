row1 = ["👀", "👀", "👀"]
row2 = ["👀", "👀", "👀"]
row3 = ["👀", "👀", "x"]
map  = [row1, row2, row3]  # this is nested list in the python program
print(f"{row1}\n{row2}\n{row3}")

position = input("Enter the position of the entry: ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[horizontal-1]
selected_row[vertical-1]
print(f"{row1}\n{row2}\n{row3}")