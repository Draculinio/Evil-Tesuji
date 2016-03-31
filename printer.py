__author__ = 'Pablo'

import board

class Printer:
    def printBoard(self,aBoard):
        cut=0
        line = ""
        for i in range(0,aBoard.getBoardTotalPositions()-1):
            if aBoard.boardList[i]==0:
                line = line+"."
            if aBoard.boardList[i]==1:
                line = line+"W"
            if aBoard.boardList[i]==2:
                line = line+"B"
            if aBoard.boardList[i]==3:
                line = line+"#"
            #line = line+str(aBoard.boardList[i])
            cut=cut+1
            if cut == aBoard.getBoardSize()+1:
                print(line+"#")
                line=""
                cut = 0
