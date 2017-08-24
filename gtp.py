__author__ = 'Pablo'

from Engine import Engine
#This class is for implementation of GTP Commands

class Gtp:
    def __init__(self):
        self.a=0
        self.command=[]

    #receives an input and resolves what to do.
    def resolve_input(self,move,board,evil_tesuji):
        move = move.upper()
        self.command=move.split()
        if self.command[0]=="VERSION":
            return self.version()
        if self.command[0]=="PLAY":
            return self.play(board)
        if self.command[0]=="GENMOVE":
            return self.genmove(self.command[1],board,evil_tesuji)


    def version(self):
        return 50,"0.0.0"
        #TODO: Quit hardcoding

    def play(self,board):
        if self.command[1]=="WHITE":
            return 2,board.coordinate_to_position(self.command[2])
        if self.command[1]=="BLACK":   
            return 1,board.coordinate_to_position(self.command[2])

    def genmove(self,color,board,evil_tesuji):
        return evil_tesuji.put_stone(color,board)