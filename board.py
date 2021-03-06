__author__ = 'Pablo Soifer'


class Board:
    """Class for Board representation"""
    def __init__(self, size):
        self.boardList = []
        self.boardSize = size
        self.totalSize = (size + 2) * (size + 1) + 1
        for i in range(0, self.totalSize):
            self.boardList.append(0)
        #BORDERS
        for i in range(0,self.boardSize+1):
            self.boardList[i] = 3
        for i in range(0,self.boardSize):
            self.boardList[(self.boardSize+1)*(i+1)]=3
        for i in range((self.boardSize+1)*(self.boardSize+1),(self.boardSize+2)*(self.boardSize+1)+1):
            self.boardList[i]=3

    #Gets a position and returns a Coordinate        
    def position_to_coordinate(self,position):
        column=['A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        finalCoord=""
        fPositionFound = False
        for row in range(1,self.boardSize):
            for col in range(0,self.boardSize):
                if col+self.boardSize+2+(row-1)*(self.boardSize+1) == position:
                    fPositionFound = True
                    finalCoord = column[col]+str(row)
                    break

        return finalCoord

    #Gets a coordinate and returns a Position
    def coordinate_to_position(self,coordinate):
        column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
        if coordinate == "PASS":
            return -5000
        if coordinate == "RESIGN":
            return -10000
        return (column.index(coordinate[0])+self.boardSize+2+(int(coordinate[1])-1)*(self.boardSize+1))

    def put_stone(self,color,position):
        self.boardList[position]=color