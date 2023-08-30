def encoder(board):
    fen_string = ""
    for rank in range(8):
        temp_str = ""
        empties=0
        for file in range(8):
            piece = board[file+rank*8]
            if piece == 0:
                empties+=1
            elif abs(piece) == 1:
                if empties:
                    temp_str += str(empties)
                    empties=0
                temp_str += 'K' if piece>0 else 'k'
            elif abs(piece) == 2:
                if empties:
                    temp_str += str(empties)
                    empties=0
                temp_str += 'P' if piece>0 else 'p'
            elif abs(piece) == 3:
                if empties:
                    temp_str += str(empties)
                    empties=0
                temp_str += 'B' if piece>0 else 'b'
            elif abs(piece) == 4:
                if empties:
                    temp_str += str(empties)
                    empties=0
                temp_str += 'N' if piece>0 else 'n'
            elif abs(piece) == 5:
                if empties:
                    temp_str += str(empties)
                    empties=0
                temp_str += 'Q' if piece>0 else 'q'
            elif abs(piece) == 6:
                if empties:
                    temp_str += str(empties)
                    empties=0
                temp_str += 'R' if piece>0 else 'r'
        if empties:
            temp_str+=str(empties)
        fen_string = temp_str + ("/" if rank else "") + fen_string 
    return fen_string