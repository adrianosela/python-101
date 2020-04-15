numbers = [1, 3, 9, 6, 0, 4, 2, 6, 5, 8, 9, 2, 5, 7, 4, 0, 1]

found = False
index = -1

while not found:
    index = index + 1
    if index > len(numbers) - 1:
        break
    if numbers[index] == 5:
        found = True

if found:
    print("first occurence of 5 happens at index", index)
else:
    print("no instances of number 5 in list")
