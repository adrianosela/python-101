### Lab 0 - Some Practical Examples

This lab will keep things simple. We will do 3 short exercises incremental in difficulty.

Review your mathematical operators, literal types, lists, conditions,
loops, and be sure to comment out your code where you deem necessary. If you are unsure about something, **take your time** and search the Internet to validate ideas you may have.

Read the questions well before beginning to work on them.

**Exercises:**

## Watering Plants Planner

You are given a list representing the amount of water
required by some plants. Your water container can hold
only 1000mL (1L) at a time. Your task is to find the
number of times you will need to fill your container in
order to water all the plants. Your container starts
empty, i.e. with 0 mL.

Assume that you can NOT begin watering a plant unless you
have all of the water you need in your container. That
is, if a plant requires 800mL of water, and you only
have 400mL in your container, you MUST refill immediately.
i.e. You can't pour half now, and half after you've refilled.

Boilerplate for your code has already been written in `wateringplants.py`, and a reasonable solution in `wateringplants_soln.py `.

## Find the 'o'

Your task is to print the (row, column) coordinates, or (x, y), of the single 'o' character in a grid, represented as a list of lists:
   
```
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
```

Hint - you can nest loops within loops as follows:

```
for <var_x> in <iterator_x>:
    for <var_y> in <interator_y>:
        <statements>
```

Boilerplate for your code has already been written in `findo.py`, and a reasonable solution in `findo_soln.py `.

## Tic-Tac-Toe Game Checker

Given a list of moves where each element is another list of size 2 corresponding to the (row, column) coordinates of the grid where they mark their respective character.

Return the winner of the game if it exists ("A" or "B"), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that the list of moves is valid (moves follow the rules of Tic-Tac-Toe), the grid is initially empty and player A will play first.

Here are some examples:

```
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"
```

```
Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins.
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
"   "    "   "    "   "    "   "    "   "    "O  "
```

```
Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"
```

```
Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
"X  "
" O "
"   "
```


Boilerplate for your code has already been written in `tictactoe.py`, and a reasonable solution in `tictactoe_soln.py`. Note that the file includes a function to test your `tictactoe()` function against some examples. Run the `tictactoe.py` file before modifying it, and see how all tests are currently failing.
