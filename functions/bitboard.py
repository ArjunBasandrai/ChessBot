import numpy as np

def getBitBoard(position):
    bitboard = 0
    for i in position:
        bitboard |= (1 << (i))

    return bitboard