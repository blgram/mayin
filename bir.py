
class A:

    board = []
    height = 9
    width = 9

    def __init__(self):
        self.setBoard()

    def setBoard(self):
        for i in range(self.height):
            self.board.append([])
            for j in range(self.width):
                self.board[i].append("O")

    def printBoard(self):
        for i in range(9):
            print("")
            for j in range(9):
                print(self.board[i][j], end='')

    def xKoy(self, arg1, arg2): # self gerek mi? 
        self.board[arg1][arg2] = 'x'

    def sayiKoy(self, arg1, arg2, num):
        self.board[arg1][arg2] = num