"""
Applies a set of moves to a tictactoe board
and returns the state of the game. 

The possible states of the game are:
  "A" - player A won the game
  "B" - player B won the game
  "Draw" - board is full, no winner
  "Pending" - the game is ongoing

Your function may assume that the moves are
valid, and there will never be repeated grid
coordinates in the same game (list of moves)

:type moves: List[List[int]]
"""
def tictactoe(moves):
    # TODO: your code here
    return ""

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
