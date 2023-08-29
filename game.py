import pygame
from functions.fen import fen_parser
from functions.pieces import getPieces
from functions.moves import getLegalMoves, Promote
from pygame.locals import *
from pygame.mouse import get_pos
from time import sleep

board,player,castle,en,half,full = fen_parser("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",getPieces())
# print(board)
# board = [6, 4, 3, 5, 1, 3, 4, 6, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, -2, -2, -2, 0, -2, -2, -2, -6, -4, -3, -5, -1, 0, -4, -6]
# board,player,castle,en,half,full = fen_parser("RK6/2ppppp1/2n5/2k6/4q3/8/2PPQPPP/8 w KQkq - 0 1",getPieces())
pygame.init()
screen_size = (800,600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Matilda")
running = True
white_sq_clr = (0xff,0xf4,0xe3)
black_sq_clr = (0x66,0x88,0x99)
sq_size=60
start_x = (screen_size[0] - 8*sq_size)/2
start_y = (screen_size[1] + 8*sq_size)/2 - sq_size
x,y = start_x,start_y

def put(img,x,y):
    screen.blit(img,(x,y))

def sq(clr,x,y):
    pygame.draw.rect(screen,clr,pygame.Rect(x,y,sq_size,sq_size))

def get_piece(value):
    val = abs(value)
    image=None
    if val == 1:
        if val==value:
            image=pygame.image.load("Assets/Pieces/W_King.png")
        else:
            image=pygame.image.load("Assets/Pieces/B_King.png")
    
    elif val == 2:
        if val==value:
            image=pygame.image.load("Assets/Pieces/W_Pawn.png")
        else:
            image=pygame.image.load("Assets/Pieces/B_Pawn.png")

    elif val == 3:
        if val==value:
            image=pygame.image.load("Assets/Pieces/W_Bishop.png")
        else:
            image=pygame.image.load("Assets/Pieces/B_Bishop.png")

    elif val == 4:
        if val==value:
            image=pygame.image.load("Assets/Pieces/W_Knight.png")
        else:
            image=pygame.image.load("Assets/Pieces/B_Knight.png")
    
    elif val == 5:
        if val==value:
            image=pygame.image.load("Assets/Pieces/W_Queen.png")
        else:
            image=pygame.image.load("Assets/Pieces/B_Queen.png")
    
    elif val == 6:
        if val==value:
            image=pygame.image.load("Assets/Pieces/W_Rook.png")
        else:
            image=pygame.image.load("Assets/Pieces/B_Rook.png")
    
    if image:
        return pygame.transform.scale(image,(sq_size,sq_size))
    else:
        return None

def put_piece(board,rank,file,x,y):
    piece = board[rank*8+file]
    if piece!=0:
        image = get_piece(piece)
        put(image,x,y)

def is_on_board(x,y):
    if (start_x <= x <= start_x + 8*sq_size) and ((start_y >= y-sq_size >= start_y - 8*sq_size)):
        return True
    return False

def get_sq(x,y):
    sq_x = (x-start_x)//sq_size
    sq_y = -(y-start_y-sq_size)//sq_size
    return int(sq_y)*8 + int(sq_x)

def render_screen(x,y):
    for rank in range(8):
        for file in range(8):
            if rank%2==0:
                sq(white_sq_clr if file%2!=0 else black_sq_clr,x,y)
            else:
                sq(white_sq_clr if file%2==0 else black_sq_clr,x,y)
            put_piece(board,rank,file,x,y)
            x+=(sq_size)
        y-=(sq_size)
        x=start_x

font = pygame.font.SysFont('cambria', 32)
checkmate_text = font.render('Checkmate', True, (255,255,0),(0,0,255))
matetextRect = checkmate_text.get_rect()
matetextRect.center = (400,300)

stalemate_text = font.render('Stalemate', True, (255,255,0),(0,0,255))
staletextRect = stalemate_text.get_rect()
staletextRect.center = (400,300)

screen.fill((0x2e,0x38,0x42))
render_screen(x,y)
while running:
    x,y = start_x,start_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mx,my = get_pos()
                if is_on_board(mx,my):
                    start_sq=get_sq(mx,my)
                    value = board[start_sq]
                    if value*player>0:
                        t = start_sq

        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                mx,my = get_pos()
                if is_on_board(mx,my):
                    legals = getLegalMoves(board,player)
                    target_sq=get_sq(mx,my)
                    move = [start_sq,target_sq]
                    if value*player > 0 and move in legals:
                        board[target_sq] = value
                        board[t] = 0
                        board = Promote(board,target_sq,player,5)
                        player = -player
                        render_screen(x,y)
                        legals = getLegalMoves(board,player)
                        if legals == 0:
                            print("Checkmate")
                            screen.blit(checkmate_text, matetextRect)
                            pygame.display.update()
                        elif legals == 1:
                            print("Stalemate")
                            screen.blit(stalemate_text, staletextRect)
                            pygame.display.update()

    pygame.display.update()