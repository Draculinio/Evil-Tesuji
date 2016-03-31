__author__ = 'Pablo'

import board
import random

class Engine:
    def __init__(self,color):
        self.color=color

    #Here is the process to put a stone.
    def putStone(self,aBoard):
        #Here goes all the magic.
        valuesList = self.getValues(aBoard)
        return self.returnChosenOne((valuesList))


    def getValues(self,aBoard):
        boardListValues = []
        for i in range(0,aBoard.getBoardTotalPositions()):
            if aBoard.boardList[i]!=0: #Edges, occupied spaces, ko
                boardListValues.append(-1000)
            else:
                boardListValues.append(random.randint(0,10))
        return boardListValues

    def returnChosenOne(self,valuesList):
        return valuesList.index(max(valuesList))