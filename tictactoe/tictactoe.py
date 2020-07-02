"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
    # Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).
    free_spaces = 0
    for row in board:
        free_spaces += row.count(EMPTY)
    if (free_spaces % 2 == 0): #initial state 9 empty spaces, and X starts
        return O
    else:
        return X

    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Each action should be represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2)
    # and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
    # Possible moves are any cells on the board that do not already have an X or an O in them.
    # Any return value is acceptable if a terminal board is provided as input.
    moves = []
    for row in range(0, 3):
        for col in range(0, 3):
            if board[row][col] is EMPTY:
                moves.append((row, col))
    return moves

    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # If action is not a valid action for the board, your program should raise an exception.
    # The returned board state should be the board that would result from taking the original input board,
    # and letting the player whose turn it is make their move at the cell indicated by the input action.
    # Importantly, the original board should be left unmodified: since Minimax will ultimately require considering many different board states
    # during its computation. This means that simply updating a cell in board itself is not a correct implementation of the result function.
    # You’ll likely want to make a deep copy of the board first before making any changes.
    #print(f"going to make a move {str(action)}")
    #newBoard = copy.deepcopy(board)
    #if action != None:
    #    if newBoard[action[0]][action[1]] == EMPTY:
    #        newBoard[action[0]][action[1]] = player(newBoard)
    #    else:
    #        raise Exception ("Invalid Move")
    #return newBoard
    board_new = copy.deepcopy(board)
    player_turn = player(board)
    if action != None:
        if board_new[action[0]][action[1]] == EMPTY:
            board_new[action[0]][action[1]] = player_turn
        else:
            raise Exception("Invalid Move")
    else:
            raise Exception ("Invalid Move")
    return board_new
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # If the X player has won the game, your function should return X. If the O player has won the game, your function should return O.
    # One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
    # You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row,
    # since that would be an invalid board state).
    # If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return None.
    # Horizontal
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] != EMPTY):
            return board[row][0]
    # Vertical
    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] != EMPTY):
            return board[0][col]
    # Diagonal
    if ((board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]) and (board[1][1] != EMPTY)):
        return board[1][1]
    #Default
    return None
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If the game is over, either because someone has won the game or because all cells have been filled without anyone winning,
    # the function should return True.
    # Otherwise, the function should return False if the game is still in progress.
    if winner(board) != None:
        return True
    else:
        if actions(board) == []:
            return True
        else:
            return False
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # If X has won the game, the utility is 1. If O has won the game, the utility is -1. If the game has ended in a tie, the utility is 0.
    # You may assume utility will only be called on a board if terminal(board) is True.
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    #raise NotImplementedError



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # The move returned should be the optimal action (i, j) that is one of the allowable actions on the board.
    # If multiple moves are equally optimal, any of those moves is acceptable.
    # If the board is a terminal board, the minimax function should return None.

    if terminal(board):
        return None

    def maxvalue(board):
        v_max = -2
        best_move = None
        if terminal(board):
            return [utility(board),None]
        for action in actions(board):
            board_new = result(board, action)
            v_action = minvalue(board_new)
            if v_action[0] > v_max:
                v_max = v_action[0]
                best_move = action
        v = [v_max, best_move]
        return v

    def minvalue(board):
        v_min = 2
        best_move = None
        if terminal(board):
            return [utility(board),None]
        for action in actions(board):
            board_new = result(board, action)
            v_action = maxvalue(board_new)
            if int(v_action[0]) < v_min:
                v_min = v_action[0]
                best_move = action
        v = [v_min, best_move]
        return v

    if player(board) == X:
        v = maxvalue(board)
    else:
        v = minvalue(board)

    return v[1]

    #raise NotImplementedError
