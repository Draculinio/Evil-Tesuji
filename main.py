__author__ = 'Pablo'

from printer import Printer
from board import Board
from Engine import Engine
from gtp import Gtp

#Initialization

#evilTesuji = Engine(1)
main_board = Board(9)
main_printer = Printer()
gtp_controler = Gtp()
evil_tesuji = Engine()
#Main loop
turn = 1
while turn!=3:
    gtp_command = input()
    color,move = gtp_controler.resolve_input(gtp_command,main_board,evil_tesuji)
    if color== 1 or color == 2: #Movement command
        if move==-5000:
            print("PASS")
        else:
            if move==-10000:
                print("RESIGN")
                turn=3
            else:
                main_board.put_stone(color,move)
                main_printer.printBoard(main_board)
    else: #Other commands
        if color == 50:
            print(move)