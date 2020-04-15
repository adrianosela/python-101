"""
Your task is to print the (x, y) coordinates of the single 'o' character
in a grid, represented as a list of lists.

Hint - you can nest loops within loops
"""

grid = [
        ["x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "o", "x"],
        ["x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x"],
    ]

for i in range(len(grid)):
    for j in range(len(grid[0])):
            if grid[i][j] == "o":
                print("coords: (%d, %d)" % (i, j))
