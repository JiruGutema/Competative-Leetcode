class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()

        n = len(matrix)
        m = len(matrix[0])
        for r in range(n):
            for c  in range(m):
                if matrix[r][c] == 0:
                    row.add(r)
                    col.add(c)
        print(row, col)
        for r in range(n):
            for c  in range(m):
                if r in row or c in col:
                    matrix[r][c] = 0
        return matrix
        
