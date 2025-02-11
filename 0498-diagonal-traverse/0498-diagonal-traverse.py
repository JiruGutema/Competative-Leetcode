class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []

        n = len(mat)       
        m = len(mat[0]) 

        ans = []
        i, j = 0, 0
        up = True

        while len(ans) < n * m:
            ans.append(mat[i][j])
            if up:
                if j == m - 1:
                    i += 1
                    up = False
                elif i == 0:
                    j += 1
                    up = False
                else:
                    i -= 1
                    j += 1
            else:
                if i == n - 1:
                    j += 1
                    up = True
                elif j == 0:
                    i += 1
                    up = True
                else:
                    i += 1
                    j -= 1

        return ans
