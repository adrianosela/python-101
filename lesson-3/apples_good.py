my_list = ["apples", "oranges", "bananas", "apples", "apples", "lemon"]

appleCount = 0

for fruit in my_list:
    if fruit == "apples":
        appleCount = appleCount + 1

print(appleCount)
