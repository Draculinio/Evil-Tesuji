__author__ = 'Pablo'

import board
import random

class Engine:
    def __init__(self):
        self.color = 0
        
    
    #Here is the process to put a stone.
    def put_stone(self,color,my_board):
        #Here goes all the magic.
        if color=="WHITE":
            self.color=2
        else:
            self.color=1
        values_list = self.getValues(my_board)
        return self.color, self.returnChosenOne((values_list))

    #Gets the values of the board
    def getValues(self,my_board):
        boardListValues = []
        for i in range(0,my_board.totalSize):
            if my_board.boardList[i]!=0: #Edges, occupied spaces, ko
                boardListValues.append(-1000)
            else:
                boardListValues.append(random.randint(0,10))
        return boardListValues

    #Returns the chosen move - Last part of the stone selection
    def returnChosenOne(self,valuesList):
        return valuesList.index(max(valuesList))