#!/usr/bin/env python3

# Terminal minesweeper
#
# John Diaz january 2023 Base on 12 beginner Python projects - Coding Course FreeCodeCamp.org
# TO DO List:
#
#

import numpy as np
import random
from scipy.spatial import distance
import re


class MinesGame:
    def __init__(self, dim, nbombs):
        self.dim = dim
        self.nbombs = nbombs
        self.board = self.make_board
        self.dug = set()


    def make_board(self):

        bombs_coords = np.zeros([self.nbombs, 2], dtype=int)
        # Plant the first bomb
        irb = random.randint(0, self.dim-1)
        icb = random.randint(0, self.dim-1)
        bombs_coords[0, 0] = irb
        bombs_coords[0, 1] = icb
        nb = 1               # Number of planted bombs
        while nb < self.nbombs:
            irb = random.randint(0, self.dim-1)
            icb = random.randint(0, self.dim-1)
            plant = False
            # Check if the next bomb is 3 nodes away from the previous
            for jb in range(nb):
                jrb = bombs_coords[jb, 0]
                jcb = bombs_coords[jb, 1]
                if distance.euclidean([irb, icb], [jrb, jcb]) > 4:
                    plant = True
                else:
                    plant = False
            if plant:
                bombs_coords[nb, 0] = irb
                bombs_coords[nb, 1] = icb
                nb += 1

        # Step 1: create the board and plant the bombs
        board = np.zeros([self.dim, self.dim], dtype=int)
        for ib in range(self.nbombs):
            irb = bombs_coords[ib, 0]
            icb = bombs_coords[ib, 1]
            # Put the bomb
            board[irb, icb] = -1
            # Put ones around the bomb
            row_ = range(self.dim)
            if irb-1 in row_:
                board[irb-1, icb] = 1
                if icb-1 in row_:
                    board[irb-1, icb-1] = 1
                if icb+1 in row_:
                    board[irb-1, icb+1] = 1

            if irb+1 in row_:
                board[irb+1, icb] = 1
                if icb-1 in row_:
                    board[irb+1, icb-1] = 1
                if icb+1 in row_:
                    board[irb+1, icb+1] = 1
            if icb-1 in row_:
                board[irb, icb-1] = 1
            if icb+1 in row_:
                board[irb, icb+1] = 1

            # Put twos two nodes way from the bomb
            if irb-1 in row_:
                if icb+2 in row_:
                    board[irb-1, icb+2] = 2
                if icb-2 in row_:
                    board[irb-1, icb-2] = 2
            if irb+1 in row_:
                if icb+2 in row_:
                    board[irb+1, icb+2] = 2
                if icb-2 in row_:
                    board[irb+1, icb-2] = 2
            if irb-2 in row_:
                board[irb-2, icb] = 2
                if icb-1 in row_:
                    board[irb-2, icb-1] = 2
                if icb+1 in row_:
                    board[irb-2, icb+1] = 2
                if icb-2 in row_:
                    board[irb-2, icb-2] = 2
                if icb+2 in row_:
                    board[irb-2, icb+2] = 2
            if irb+2 in row_:
                board[irb+2, icb] = 2
                if icb-1 in row_:
                    board[irb+2, icb-1] = 2
                if icb+1 in row_:
                    board[irb+2, icb+1] = 2
                if icb-2 in row_:
                    board[irb+2, icb-2] = 2
                if icb+2 in row_:
                    board[irb+2, icb+2] = 2
            if icb-2 in row_:
                board[irb, icb-2] = 2
            if icb+2 in row_:
                board[irb, icb+2] = 2

        return board

    def Dig(self, rirow, icol):
        pass

    def __str__(self):
        string_ = ' '
        # first let's create a new array that represents what the user will see
        visible_board = [[None for _ in range(self.dim)]
                        for _ in range(self.dim)]
        for row in range(self.dim):
            for col in range(self.dim):
                # if (row,col) in self.dug:
                #    visible_board[row][col] = str(self.board[row][col])
                # else:
                visible_board[row][col] = ' '

        return string_


def ini_visual_board(dim):
    visible_board = [['#' for _ in range(dim)] for _ in range(dim)]
    rang = [str(ir) for ir in range(dim)]

    print('   ', " ".join(rang))
    for ir in range(dim):
        print('  '+str(ir), " ".join(visible_board[ir]))

    return visible_board


def init_debug():
    with open("minesweeper.out", "w") as f:
        f.write('\n')
        f.write(' minesweeper debug file \n')


def write_debug(msg):
    with open("minesweeper.out", "a") as f:
        f.write("\n")    
        f.write(msg)
        f.write("\n")


if __name__ == '__main__':
    # Open debugging output file
    init_debug()

    # Initiate board object
    dim = 6                                      # Size of board dimxdim  
    mines = 2                                    # Number of mines
    game = MinesGame(dim, mines)
    board = game.board()
    visual_board = ini_visual_board(dim)
    rang = [str(ir) for ir in range(dim)]

    write_debug(' Starting visible board ')
    write_debug(' rang: ' + str(rang))
    write_debug(' visible_board: ' + str(visual_board))

    print()
    while len(game.dug) < game.dim ** 2 - game.nbombs:
        # 0,0 or 0, 0 or 0,    0
        print()
        user_input = re.split(
            ',(\\s)*', input("Where would you like to dig? Input as row,col: "))  # '0, 3'
        row, col = int(user_input[0]), int(user_input[-1])
        write_debug(f' Dug row and col: {row}, {col} ')
        game.dug.add((row, col))  # keep track where user dug 
        print()
        visual_board[row][col] = str(board[row, col])
        print('   ', " ".join(rang))
        write_debug('    ' + str(rang))
        for ir in range(dim):
            print('  '+str(ir), " ".join(visual_board[ir]))
            write_debug('  '+str(ir) + str(visual_board))

        if board[row, col] == -1:
            print()
            print(" Cataplump!!!!! you dig a bomb, game over...")
            break

    print()
    if len(game.dug) == dim**2 - mines:
        print(" Congratulation !!!!")
