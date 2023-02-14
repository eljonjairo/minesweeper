#!/usr/bin/env python3

# Terminal minesweeper
# 
# John Diaz january 2023 Base on 12 beginner Python projects - Coding Course FreeCodeCamp.org
#TO DO List:
#  
#

import numpy as np
import random
from scipy.spatial import distance
import re

class Board:
    def __init__(self, dim, nbombs):
        self.dim = dim
        self.nbombs = nbombs
        self.board = self.makeBoard
        self.dug = set()
        
    def makeBoard(self):

    
        BombsCoords = np.zeros([self.nbombs,2], dtype = int)
        # Plant the first bomb
        irb = random.randint(0,self.dim-1)
        icb = random.randint(0,self.dim-1)
        BombsCoords[0,0] = irb
        BombsCoords[0,1] = icb
        nb = 1               # Number of planted bombs
        while nb < self.nbombs:
            irb = random.randint(0,self.dim-1)
            icb = random.randint(0,self.dim-1)
            plant = False
            # Check if the next bomb is 3 nodes away from the previous 
            for jb in range (nb):
                jrb = BombsCoords[jb,0]
                jcb = BombsCoords[jb,1]
                if distance.euclidean([irb,icb],[jrb,jcb]) > 4:
                    plant = True
                else:
                    plant = False
            if plant:
                BombsCoords[nb,0] = irb
                BombsCoords[nb,1] = icb
                nb += 1
        
        #Step 1: create the board and plant the bombs
        Board = np.zeros([self.dim,self.dim], dtype = int)
        for ib in range(self.nbombs):
            irb = BombsCoords[ib,0]
            icb = BombsCoords[ib,1]
            # Put the bomb
            Board[irb,icb] = -1
            # Put ones around the bomb
            row_ = range(self.dim)
            if irb-1 in row_:
                Board[irb-1,icb] = 1
                if icb-1 in row_:
                    Board[irb-1,icb-1] = 1
                if icb+1 in row_:        
                    Board[irb-1,icb+1] = 1
                    
            if irb+1 in row_:        
                Board[irb+1,icb] = 1   
                if icb-1 in row_:    
                   Board[irb+1,icb-1] = 1
                if icb+1 in row_:        
                   Board[irb+1,icb+1] = 1      
            if icb-1 in row_:    
                Board[irb,icb-1] = 1   
            if icb+1 in row_:        
                Board[irb,icb+1] = 1  
        
            # Put twos two nodes way from the bomb
            if irb-1 in row_:
                if icb+2 in row_:
                    Board[irb-1,icb+2] = 2
                if icb-2 in row_:
                    Board[irb-1,icb-2] = 2    
            if irb+1 in row_:
                if icb+2 in row_:
                    Board[irb+1,icb+2] = 2
                if icb-2 in row_:
                    Board[irb+1,icb-2] = 2
            if irb-2 in row_:
                Board[irb-2,icb] = 2
                if icb-1 in row_:
                    Board[irb-2,icb-1] = 2
                if icb+1 in row_:        
                    Board[irb-2,icb+1] = 2
                if icb-2 in row_:
                    Board[irb-2,icb-2] = 2
                if icb+2 in row_:        
                    Board[irb-2,icb+2] = 2
            if irb+2 in row_:
                Board[irb+2,icb] = 2
                if icb-1 in row_:
                    Board[irb+2,icb-1] = 2
                if icb+1 in row_:        
                    Board[irb+2,icb+1] = 2
                if icb-2 in row_:
                    Board[irb+2,icb-2] = 2
                if icb+2 in row_:        
                    Board[irb+2,icb+2] = 2
            if icb-2 in row_:    
                Board[irb,icb-2] = 2   
            if icb+2 in row_:    
                Board[irb,icb+2] = 2   
            
        return Board    

    def Dig(self,rirow,icol):
        pass


    
    def __str__(self):
        string_ = ' '
        # first let's create a new array that represents what the user would see
        visibleBoard = [[None for _ in range(self.dim)] for _ in range(self.dim)]
        for row in range(self.dim):
            for col in range(self.dim):
                #if (row,col) in self.dug:
                #    visible_board[row][col] = str(self.board[row][col])
                # else:
                visibleBoard[row][col] = ' '

       
        return string_

def iniVisualBoard(dim):
    VBoard = [['#' for _ in range(dim)] for _ in range(dim)]
    rang = [str(ir) for ir in range(dim)] 
        
    print('   '," ".join(rang))
    for ir in range(dim):
        print('  '+str(ir)," ".join(VBoard[ir]))

    return VBoard

if __name__ == '__main__':
     NewBoard = Board(6,2)
     print()
     Board = NewBoard.board()
     VBoard = iniVisualBoard(NewBoard.dim)
     rang = [str(ir) for ir in range(NewBoard.dim)] 
     while len(NewBoard.dug) < NewBoard.dim ** 2 - NewBoard.nbombs :
        # 0,0 or 0, 0 or 0,    0
        print()
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))  # '0, 3'
        row, col = int(user_input[0]), int(user_input[-1])
        NewBoard.dug.add((row, col)) # keep track that we dug here
        print()
        VBoard[row][col] = str(Board[row,col])
        print('   '," ".join(rang))
        for ir in range(NewBoard.dim):
            print('  '+str(ir)," ".join(VBoard[ir]))        
            
        if Board[row,col] == -1:
            print()
            print(" Cataplump!!!!! you dig a bomb, game over...")
            break
    
     print()
     if len(NewBoard.dug) == NewBoard.dim ** 2 - NewBoard.nbombs:
         print(" Congratulation !!!!")       
    
    
