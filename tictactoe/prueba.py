import tictactoe as ttt

board = ttt.initial_state()
newBoard = None
#X
ttt.result(board, (0, 0))
print(newBoard)
#O
ttt.result(board, (1, 0))
#X
ttt.result(board, (0, 1))
#O
ttt.result(board, (1, 1))
#X
ttt.result(board, (1, 2))
#O
ttt.result(board, (0, 2))
#X
#ttt.result(board, (2, 2))
#O
#ttt.result(board, (2, 1))


print("TURNO 1")
#print(ttt.minimax(board))
print(board)
move = ttt.minimax(board)
print(move)
print("finalizo")
print(board)
