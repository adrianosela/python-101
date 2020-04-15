numbers = [1, 3, 9, 6, 0, 4, 2, 6, 5, 8, 5, 9, 2, 7, 4, 0, 1]

found = False
index = -1

while(not found):
    index = index + 1
    if numbers[index] == 5:
        found = True
    
print("first occurence of 5 happens at index", index)
