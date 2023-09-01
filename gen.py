import copy
from functions.moves import getLegalMoves, makeMove
from functions.fen import fen_parser
from functions.pieces import getPieces
from time import time

def movegen(board, player, castle, en, halfmove, fullmove, moves_history, depth):
    if depth == 0:
        return 1
    positions = 0
    moves, new_castle = getLegalMoves(board, player, castle, en, halfmove, moves_history)
    if type(moves) != list:
        print("hola")
        return 1
    for move in moves:
        temp_board = copy.deepcopy(board)  
        temp_castle = copy.deepcopy(new_castle) 
        temp_board, temp_castle, new_en, new_halfmove, new_fullmove, new_moves_history = makeMove(temp_board, move[0], move[1], board[move[0]], player, temp_castle, en, halfmove, fullmove, list(moves_history))
        positions += movegen(temp_board, -player, temp_castle, new_en, new_halfmove, new_fullmove, new_moves_history, depth - 1)
    return positions

board, player, castle, en, halfmove, fullmove = fen_parser("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", getPieces())
moves_history = []

start_time = time()
positions = movegen(board, player, castle, en, halfmove, fullmove, moves_history, 3)
end_time = time()

elapsed_time = (end_time-start_time)*1000
print(positions, elapsed_time)
