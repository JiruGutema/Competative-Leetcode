class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        newMatrix = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(col):
                newMatrix[j][i] = matrix[i][j]
        return newMatrix