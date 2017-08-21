__author__ = 'Pablo'

import board
import random

class Engine:
    def __init__(self,color):
        self.color=color
        self.gtpEngine=gtp()

    #This is to receive values, connects with gtp engine
    def receive_value(self,my_board):
        move = input()
        self.gtpEngine.resolve_input(move,my_board)

    
    #Here is the process to put a stone.
    def putStone(self,my_board):
        #Here goes all the magic.
        values_list = self.getValues(my_board)
        return self.returnChosenOne((values_list))

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