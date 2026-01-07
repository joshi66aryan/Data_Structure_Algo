class NQueen:
    def __init__(self,n):
        self.n = n
        self.chess_table = [[0 for i in range(n)] for j in range(n)]

    def printQueen(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print("Q",end='')
                else:
                    print("-",end='')
            print()

    def is_place_valid(self,row_index, column_index):

        # check to the left from positioned index in row
        for i in range(self.n):
            if self.chess_table[row_index][i] == 1:
                return False

        # check to the top left diagonal
        j = column_index
        for i in range(row_index, -1, -1):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j =j - 1
            if j < 0:
                break

        #check to the bottom left diagonal
        j = column_index
        for i in range(row_index, self.n):
            if i< 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j = j-1
            if j < 0:
                break
        
        return True

    def solve(self,col_index):
        if col_index == self.n:
            return True
        
        for i in range(self.n):
            if self.is_place_valid(i,col_index):
                self.chess_table[i][col_index] = 1

                if self.solve(col_index+1):
                    return True
            
                self.chess_table[i][col_index] = 0
        return False

    def solve_NQueen(self):
        if self.solve(0):
            self.printQueen()
        else:
            print("There isn't any solution for this problem!")
        
queen = NQueen(4)
queen.solve_NQueen()
