__author__ = 'Pablo'

from printer import Printer
from board import Board
from Engine import Engine

evilTesuji = Engine(2)
mainBoard = Board(9)
mainPrinter = Printer()
mainPrinter.printBoard(mainBoard)
move = evilTesuji.putStone(mainBoard)
mainBoard.putStone(move,evilTesuji.color)
print(mainBoard.posToCoordinate(move))
mainPrinter.printBoard(mainBoard)