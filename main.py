__author__ = 'Pablo'

from printer import Printer
from board import Board
from Engine import Engine
from gtp import Gtp

#Initialization

evilTesuji = Engine(1)
mainBoard = Board(9)
mainPrinter = Printer()

#Main loop

turn = 1
while turn!=3:
    #move = mainBoard.coordinateToPosition(gtpControler.receive_input())
mainBoard.boardList[move]=evilTesuji.color
#mainBoard.putStone(move,evilTesuji.color)
#print(mainBoard.posToCoordinate(move))
mainPrinter.printBoard(mainBoard)
mainPrinter.printSomething(mainBoard.posToCoordinate(move))
mainPrinter.printSomething(mainBoard.coordinate_to_position(mainBoard.posToCoordinate(move)))

