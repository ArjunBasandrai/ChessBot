import numpy as np

def fen_parser(fen_code,pieces):

    fen_code = fen_code.split(' ')
    player=1
    halfmove,fullmove=0,0
    castle=[0,0,0,0]
    en=None
    board = np.full(8*8,0)

    row,col=0,0

    for stage in fen_code:
        stage_idx = fen_code.index(stage)

        for char in stage:
            if char == " ":
                break

            if stage_idx == 0:
                if char.isdigit():
                    col+=int(char)

                elif char=='/':
                    col=0
                    row+=1
                
                else:
                    if char.isupper():
                        board[row*8+col] = pieces[char.lower()]
                    else:
                        board[row*8+col] = -pieces[char]
                    col+=1
            elif stage_idx == 1:
                if char == 'w':
                    player = 1
                elif char == 'b':
                    player = -1
                
            elif stage_idx == 2:
                if char == '-':
                    break
                if char=="K":
                    castle[0]=1
                elif char=="Q":
                    castle[1]=1
                elif char=="k":
                    castle[2]=1
                elif char=="q":
                    castle[3]=1
                
            elif stage_idx == 3:
                if char == "-":
                    break
                else:
                    en = stage
            
            elif stage_idx in (4,5):
                if stage.isdigit():
                    if stage_idx==4:
                        halfmove=int(stage)                
                    else:
                        fullmove=int(stage)

    board = list(reversed(list((zip(*[iter(board)]*8)))))
    board = [j for i in board for j in i]
    return board,player,castle,en,halfmove,fullmove