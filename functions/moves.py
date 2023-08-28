directionOffsets = [8, -8, -1, 1, 7, -7, 9, -9]
numSquaresToEdge = []

for rank in range(8):
    for file in range(8):
        N = 7 - rank
        S = rank
        W = file
        E = 7 - file

        numSquaresToEdge.append([
            N,S,W,E,
            min(N,W),
            min(S,E),
            min(N,E),
            min(S,W)
        ])


def getSlidingMoves(board,start_square,piece,player,legalMoves):
    start = 4 if abs(piece)==3 else 0
    end = 4 if abs(piece)==6 else 8
    for direction in range(start,end):
        for n in range(0,numSquaresToEdge[start_square][direction]):
            target_square = start_square + directionOffsets[direction] * (n+1)
            target_piece = board[target_square]
            if target_piece and target_piece//abs(target_piece) == player:
                break
            legalMoves.append([start_square,target_square])
            if target_piece and target_piece//abs(target_piece) == -player:
                break
    return legalMoves

def getPawnMoves(board,start_square,player,legalMoves):
    direction = 0 if player==1 else 1
    offsets = range(2) if ((start_square in range(8,16) and player == 1)) or ((start_square in range(48,56) and player == -1)) else range(1)
    for n in offsets:
        target_square = start_square + directionOffsets[direction] * (n+1)
        target_piece = board[target_square]
        if target_piece and target_piece//abs(target_piece) == player:
            break
        if target_piece and target_piece//abs(target_piece) == -player:
            break
        legalMoves.append([start_square,target_square])
    
    directions = [4,6] if player==1 else [5,7]
    for direction in directions:
        target_square = start_square + directionOffsets[direction]
        target_piece = board[target_square]
        if target_piece and target_piece//abs(target_piece) == -player:
            legalMoves.append([start_square,target_square])
    
    return legalMoves

def getKingMoves(board,start_square,player,legalMoves):
    for direction in range(8):
        for _ in range(0,numSquaresToEdge[start_square][direction]):
            target_square = start_square + directionOffsets[direction]
            target_piece = board[target_square]
            if target_piece and target_piece//abs(target_piece) == player:
                break
            legalMoves.append([start_square,target_square])
            if target_piece and target_piece//abs(target_piece) == -player:
                break
    return legalMoves

def getKnightMoves(board,start_square,player,legalMoves):
    for direction in range(4):
        if numSquaresToEdge[start_square][direction] >= 2:
            intermediate_square = start_square + directionOffsets[direction] * 2
            halfstep_directions = [2,3] if direction in [0,1] else [0,1]
            for halfstep in halfstep_directions:
                if numSquaresToEdge[intermediate_square][halfstep] >= 1:
                    target_square = intermediate_square + directionOffsets[halfstep] * 1
                    target_piece = board[target_square]
                    if target_piece and target_piece//abs(target_piece) == player:
                        break
                    legalMoves.append([start_square,target_square])
                    if target_piece and target_piece//abs(target_piece) == -player:
                        break
    return legalMoves

def getLegalMoves(board,player,legalMoves):
    legalMoves=[]
    for square in range(64):
        piece = board[square]
        if piece!=0:
            if piece//abs(piece) == player:
                if abs(piece) in (3,5,6):
                    legalMoves = getSlidingMoves(board,square,piece,player,legalMoves)
                if abs(piece) == 2:
                    legalMoves = getPawnMoves(board,square,player,legalMoves)
                if abs(piece) == 1:
                    legalMoves = getKingMoves(board,square,player,legalMoves)
                if abs(piece) == 4:
                    legalMoves = getKnightMoves(board,square,player,legalMoves)
    return legalMoves