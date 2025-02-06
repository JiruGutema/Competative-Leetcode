class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat) 
        for _ in range(4):
            if mat == target:
                return True
            newmat = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    newmat[j][n - 1 - i] = mat[i][j]
            
            mat = newmat
        
        return mat == target  