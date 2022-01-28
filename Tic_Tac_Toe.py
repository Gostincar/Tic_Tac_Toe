import pygame
import numpy as np
import sys
from flask import Flask

app = Flask(__name__)
pygame.init() # Initializing pygame module


height = 600
width = 600
screen = pygame.display.set_mode((width, height)) # Creating a screen
pygame.display.set_caption("Tic Tac Toe") # Creating the title
BG_color = (28, 170, 156)
screen.fill(BG_color)
Red = (255, 0, 0)
board_rows = 3
board_cols = 3
line_width = 15
line_color = (14, 145, 155)
circle_radius = 60
circle_width = 15
circle_color = (239, 235, 100)
cross_width = 15
space =50
cross_color = (66, 66, 66)
# board with numpy
board = np.zeros((board_rows, board_cols))

#pygame.draw.line(screen, Red, (10, 10), (200, 200), 10)  # getting red line
# Creating lines on the screen
def draw_lines():
# first horizontal
    pygame.draw.line(screen,line_color,(0,200),(600,200), line_width)
# second horizontal
    pygame.draw.line(screen, line_color,(0, 400), (600, 400), line_width)
# first vertikal
    pygame.draw.line(screen, line_color,(200, 0), (200, 600), line_width)
# second vertical
    pygame.draw.line(screen, line_color,(400, 0), (400, 600), line_width)

def draw_figures():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:  # if player1 has marked the square
                # drawing the circle
                pygame.draw.circle(screen, circle_color, (int(col * 200 + 100), int(row * 200 + 100)), circle_radius, circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen, cross_color, (col * 200+space, row * 200 + 200- space), (col * 200 + 200-space, row * 200+space), cross_width)
                pygame.draw.line(screen, cross_color, (col * 200+space, row * 200 + space), (col * 200 + 200-space, row * 200+200-space), cross_width)


def mark_square( row, col, player):
    board[row][col] = player
# function that returns true if square is available, and false if it's not
def available_square(row, col):
    # return board[row][col]==0:
    if board[row][col] == 0:
        return True

    else:
        return False
# Code that is telling us is the board is full or not ? If we fund enmpy sqare,
# it retuns false
def is_board_full():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    # checking vertical line
    for col in range(board_cols) :
        if board[0][col] == player and board[1][col] == player and board[2][col] == player :
            draw_vertical_winning_line(col,player)
            return True
    # checking horisontal line
    for row in range(board_rows) :
        if board[0][row] == player and board[1][row] == player and board[2][row] == player :
            draw_horizonlat_winning_line(row,player)
            return True
    # assending diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player :
        draw_asc_diagonal(player)
    # descending  diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True
    return False
def draw_vertical_winning_line(col,player):
    posX = col*200 + 100
    if player == 1 :
        color = circle_color
    elif player == 2 :
        color = cross_color
    pygame.draw.line(screen, color, (posX,15),(posX, height - 15),15)


def draw_horizonlat_winning_line(row,player):
    posY = row * 200 + 100
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color, (15,posY), ( width - 15, posY), 15)
def draw_asc_diagonal(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color, (15, height-15), (width -15,15),15)
def draw_desc_diagonal(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color,(15,15),(width-15, height-15),15)


def restart():
    screen.fill(BG_color)
    draw_lines()
    player = 1
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] == 0

'''
# returning false
print(is_board_full())
for row in range(board_rows):
    for col in range(board_cols):
        mark_square(row, col, 1)
# returning True , couse we marked squares
print(is_board_full())
'''
draw_lines()
player = 1
game_over = False
# Creating the main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            # acessing X,Y Cord, when we are clicking the screen
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200) # 200 is lenght of each square
            clicked_col = int(mouseX // 200) # // - rounds the numbber
            # print(clicked_row) , when we click 1st square
            #print(clicked_col) it retunds 0,0 ( 2nd - 0,1 )
            if available_square(clicked_row, clicked_col):

                if player == 1:
# when player == 1 it means that, player1 has marked the square, and it's
# time for player2 to play
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1
                draw_figures()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_r:
                restart()
    pygame.display.update() # Updating the main loop



app.run()
