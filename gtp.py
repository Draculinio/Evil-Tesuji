__author__ = 'Pablo'

#This class is for implementation of GTP Commands

class Gtp:
    def __init__(self):
        self.a=0
        self.command=[]

    #receives an input and resolves what to do.
    def resolve_input(self,move,board):
        move = move.upper()
        self.command=move.split()
        if self.command[0]=="VERSION":
            return self.version()
        if self.command[0]=="PLAY":
            return self.play(board)

                


    def version(self):
        return 50,"0.0.0"
        #TODO: Quit hardcoding

    def play(self,board):
        if self.command[1]=="B":
            return 1,board.coordinate_to_position(self.command[2])
        if self.command[1]=="W"    
            return 2,board.coordinate_to_position(self.command[2])