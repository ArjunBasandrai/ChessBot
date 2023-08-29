import numpy as np

def getBitBoard(position):
    bitboard = np.int64(0)

    for i in position:
        bitboard |= (np.int64(1) << (i))
    
    return bitboard