__author__ = 'Pablo'

#Everything that is printed by console goes here, noting in the main  py

import board

class Printer:
    def printBoard(self,aBoard):
        column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
        rowCounter=0
        cut=0
        line = ""
        colCounter = " "
        for i in range(0,aBoard.boardSize):
            colCounter=colCounter+column[i]
        print(colCounter)
        for i in range(0, aBoard.totalSize-1):
            if aBoard.boardList[i]==0:
                line = line+"."
            if aBoard.boardList[i]==1:
                line = line+"B"
            if aBoard.boardList[i]==2:
                line = line+"W"
            if aBoard.boardList[i]==3:
                line = line+"#"
            cut=cut+1
            if cut == aBoard.boardSize+1:
                if rowCounter>=1 and rowCounter<=aBoard.boardSize:
                    print(line+"#"+str(rowCounter))
                else:
                    print(line + "#")
                rowCounter=rowCounter+1
                line=""
                cut = 0

    def print_something(self,text):
        print(text)