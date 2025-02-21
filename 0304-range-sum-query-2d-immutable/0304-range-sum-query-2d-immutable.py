class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        row = len(matrix)
        col = len(matrix[0])
        direction = [(-1,-1),(-1,0),(0,-1)]
        for r in range(row):
            for c in range(col):
                temp = self.matrix[r][c]
                for dr, dc in direction:
                    rr = dr+r
                    cc = dc+c
                    if 0<= rr < row and 0<= cc < col:
                        if dr == -1 and dc == -1:
                            temp -= self.matrix[rr][cc]
                        else:
                            temp += self.matrix[rr][cc]
                self.matrix[r][c] = temp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rect1 = self.matrix[row2][col2]
        rect2 = self.matrix[row1-1][col2] if row1 > 0 else 0
        rect3 = self.matrix[row2][col1-1] if col1 > 0 else 0
        rect4 = self.matrix[row1-1][col1-1] if col1 > 0 and row1 > 0 else 0
        return  rect1 - rect2 - rect3 + rect4
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)