### tic tac toe
import copy
import random
import sys

import numpy as np
import pygame
from numpy.ma.core import empty, squeeze

from CONSTANTS_TTT import *


#PYGAME
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TTT AI')
screen.fill(BG_COLOR)

#always initialize while making new game
class Board:

    def __init__(self):
        self.squares = np.zeros((ROWS,COLS))
        self.empty_sqrs =  self.squares
        self.marked_sqrs = 0

        print(self.squares)

    def final_state(self ,show=False):
        '''
        RETURN 0 IF THERE IS NO WIN YET , DOESNT MEAN NO DRAW ,
        BUT IF THE BOARD IS FULL AND THE RETURN IS STILL 0 THEN IT IS A DRAW

        RETURN 1 IF PLAYER 1 WINS

        RETURN 2 IF PLAYER 2 WINS

        :return:
        '''

        #VERTICAL WINS
        for col in range(COLS):
            #this will be make sure all are 1 or 2 but not all are 0 which makes sense
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] !=0 :
                if show:
                    color = CIRC_COLOR if self.squares[0][col] == 2 else X_COLOR
                    iPos = ( col * SQSIZE + SQSIZE // 2 , 20)
                    fPos = ( col * SQSIZE + SQSIZE // 2 , HEIGHT - 20)
                    pygame.draw.line(screen , color , iPos , fPos ,LINE_WIDTH)
                return self.squares[1][col]

        # VERTICAL WINS
        for row in range(ROWS):
            # this will be make sure all are 1 or 2 but not all are 0 which makes sense
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[row][0] == 2 else X_COLOR
                    iPos = (20, row * SQSIZE + SQSIZE // 2)
                    fPos = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[row][1]

        #DIAGONAL  WINS
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                color = CIRC_COLOR if self.squares[1][1] == 2 else X_COLOR
                iPos = (20, 20)
                fPos = (WIDTH - 20, HEIGHT - 20)
                pygame.draw.line(screen, color, iPos, fPos, X_WIDTH)
            return self.squares[1][1]

        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] !=0:
            if show:
                color = CIRC_COLOR if self.squares[1][1] == 2 else X_COLOR
                iPos = (20, HEIGHT - 20)
                fPos = (WIDTH - 20, 20)
                pygame.draw.line(screen, color, iPos, fPos, X_WIDTH)
            return self.squares[1][1]

        #no win yet
        return 0

    def mark_sqr(self,row,col,player):
        self.squares[row][col]=player
        self.marked_sqrs+=1



    def empty_sqr(self,row,col):
        #if it is true
        return self.squares[row,col]==0

    def get_empty_sqrs(self):
        empty_sqrs =[]
        for row in range(ROWS) :
            for col in range(COLS):
                if self.empty_sqr(row,col):
                    empty_sqrs.append((row,col))

        return empty_sqrs


    def isfull(self):
        return self.marked_sqrs == 9

    def isempty(self):
        return self.marked_sqrs == 0

class AI :
    def __init__(self , level = 1 , player = 2 ):
        self.player = player
        self.level = level

    def rnd(self,board):
        empty_sqrs = board.get_empty_sqrs()
        idx = random.randrange(0,len(empty_sqrs))
        return empty_sqrs[idx]

    def minimax(self,board ,maximizing,alpha=-100 , beta = 100):
        #terminal cases check
        case = board.final_state()
        #player
        if case == 1 :
            return 1,None #eval , Move

        #ai
        if case == 2:
            return -1,None #eval , Move

        #draw
        elif board.isfull():
            return 0,None

        if maximizing:
            maxeval = -100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, 1)
                reval = self.minimax(temp_board, False,alpha , beta)[0]

                if reval>maxeval:
                    maxeval = reval
                    best_move = (row, col)

                alpha= max(alpha , reval)
                if alpha>=beta:
                    break

            return maxeval, best_move


        elif not maximizing:
            mineval = +1000
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, 2)
                reval = self.minimax(temp_board,True, alpha , beta )[0]

                if mineval > reval :
                    mineval = reval
                    best_move = (row,col)
                beta = min(beta , reval)
                if alpha >= beta:
                    break

            return mineval , best_move


    def eval(self,main_board):
        if self.level == 0 :
            aeval = 'random'
            move = self.rnd(main_board)

        else:
            aeval,move = self.minimax(main_board, False)

        print(f'AI HAS CHOSEN TO MARK THE SQUARE IN POS{move} with an eval of {aeval}')

        return move #row,col

class Game:
    def __init__(self):
        self.board=Board()
        self.player=2 #cross and 2 = circles
        self.ai = AI()
        self.gamemode = 'ai'
        self.running = True
        self.lines_show()

    def make_move(self,row,col):
        self.board.mark_sqr(row, col, self.player)
        self.draw_fig(row, col)
        self.next_turn()

    def lines_show(self):
        screen.fill(BG_COLOR)
        #vertical lines
        pygame.draw.line(screen,LINE_COLOR,(SQSIZE,0),(SQSIZE,HEIGHT),LINE_WIDTH)
        pygame.draw.line(screen,LINE_COLOR,(WIDTH-SQSIZE,0),(WIDTH-SQSIZE,HEIGHT),LINE_WIDTH)

        #HORIZONTAL LINES
        pygame.draw.line(screen,LINE_COLOR,(0,HEIGHT-2*SQSIZE),(HEIGHT,HEIGHT-2*SQSIZE),LINE_WIDTH)
        pygame.draw.line(screen,LINE_COLOR,(0,HEIGHT-SQSIZE),(HEIGHT,HEIGHT-SQSIZE),LINE_WIDTH)

    def draw_fig(self,row,col):
        if(self.player ==1):

            start_desc = (col * SQSIZE +OFFSET , row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)

            pygame.draw.line(screen,X_COLOR,start_desc , end_desc , X_WIDTH)

            start_asc =( col * SQSIZE + OFFSET , row*SQSIZE + SQSIZE -OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET , row * SQSIZE +OFFSET)

            pygame.draw.line(screen,X_COLOR,start_asc , end_asc , X_WIDTH)


        if(self.player == 2):
            center=(col * SQSIZE +SQSIZE //2 , row * SQSIZE +SQSIZE//2)
            pygame.draw.circle(screen, CIRC_COLOR, center, CIRC_RADIUS,CIRC_WIDTH)

    def next_turn(self):
        #changes from player 1 to player 2 and vice versa
        self.player = self.player% 2 + 1

    def change_gamemode(self):
        self.gamemode = 'ai ' if self.gamemode == 'pvp' else 'pvp'


    def isover(self):
        return self.board.final_state(True) != 0 or self.board.isfull()



    def restart(self):
        self.board.__init__()
        self.__init__()

def main():

    game = Game()
    board = game.board
    ai = game.ai


    #main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.KEYDOWN:
                # g gamemode
                if event.key == pygame.K_g:
                    game.change_gamemode()


                # r restart
                if event.key == pygame.K_r:
                    game.restart()
                    game.ai = ai
                    game.board = board


                # 0 random ai
                if event.key == pygame.K_0:
                    ai.level = 0

                if event.key == pygame.K_1:
                    ai.level = 1

            # human turn
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.pos)
                # coordinates of the click
                pos = event.pos
                row = pos[1] // SQSIZE  # y axis
                col = pos[0] // SQSIZE  # x axis

                # if it is not marked
                if board.empty_sqr(row, col) and game.running:
                    game.make_move(row, col)

                    if game.isover():
                        game.running = False

        #ai turn
        if game.gamemode == 'ai' and game.player == ai.player and game.running:
            #this will update the string
            pygame.display.update()

            #ai methods
            row, col=ai.eval(board)
            game.make_move(row,col)


            if game.isover():
                game.running = False

        pygame.display.update()

#main loop will be here

main()
