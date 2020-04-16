"""
Applies a set of moves to a tictactoe board
and returns the state of the game.

The possible states of the game are:
  "A" - player A won the game
  "B" - player B won the game
  "Draw" - board is full, no winner
  "Pending" - the game is ongoing

:type moves: List[List[int]]
"""
def tictactoe(moves):
    # optimize to return quickly
    # in games with too few moves
    # (this cond. is not necessary)
    if len(moves) < 5:
        return "Pending"
    
    # define game entities
    players = ("A", "B")
    grid = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    
    # add all moves to grid alternating player
    i = 0
    for move in moves:
        row, col = move[0], move[1]
        grid[row][col] = players[i%2]
        i+=1
        
    # check whether one of the players won game
    for player in players:
        if (
            # check diagonals
            (grid[0][0] == player and grid[1][1] == player and grid[2][2] == player) or
            (grid[2][0] == player and grid[1][1] == player and grid[0][2] == player) or
            # check rows
            (grid[0][0] == player and grid[0][1] == player and grid[0][2] == player) or
            (grid[1][0] == player and grid[1][1] == player and grid[1][2] == player) or
            (grid[2][0] == player and grid[2][1] == player and grid[2][2] == player) or
            # check columns
            (grid[0][0] == player and grid[1][0] == player and grid[2][0] == player) or
            (grid[0][1] == player and grid[1][1] == player and grid[2][1] == player) or
            (grid[0][2] == player and grid[1][2] == player and grid[2][2] == player)):
                return player

    # no player won the game, and the board
    # is full, so there is a draw
    if len(moves) == 9:
        return "Draw"
    
    # the board was not full and nobody won
    # so the game must be pending
    return "Pending"

"""
checks whether a given set of moves corresponds
to the expected result

:type moves: List[List[int]]
:type expected: str
"""
def tictactoe_test(moves, expected):
    print("checking tictactoe("+ str(moves) + ")")
    result = tictactoe(moves)
    if result  == expected:
        print("[PASS]")
    else:
        print("[FAIL] expected \"%s\", got \"%s\"" % (expected, result))

tictactoe_test([[0,0],[2,0],[1,1],[2,1],[2,2]], "A")
tictactoe_test([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]], "B")
tictactoe_test([[0,0],[1,1],[0,1],[0,2],[1,0],[2,1]], "Pending")
tictactoe_test([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]], "Draw")
