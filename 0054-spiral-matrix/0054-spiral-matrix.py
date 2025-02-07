class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        right, down, left, up = True, False, False, False
        count = [0, 0, 0, 0]
        r, c = 0, 0

        ans = []
        while len(ans) < m * n:
            if right:
                while c < n - count[0]:
                    ans.append(matrix[r][c])
                    c += 1
                c -= 1
                right = False
                down = True
                r += 1
                count[0] += 1
            elif down:
                while r < m - count[1]:
                    ans.append(matrix[r][c])
                    r += 1
                r -= 1
                down = False
                left = True
                c -= 1
                count[1] += 1
            elif left:
                while c > -1 + count[2]:
                    ans.append(matrix[r][c])
                    c -= 1
                c += 1
                left = False
                up = True
                r -= 1
                count[2] += 1
            else:
                while r > -1 + count[3] + 1:
                    ans.append(matrix[r][c])
                    r -= 1
                r += 1
                up = False
                right = True
                c += 1
                count[3] += 1


        return ans












        """turning = [(row,0), (0, col), (row, col), (0, row)

        for ind, point in enumerate(turning):
            for i in range():
                for j in range()
            
            ind = 0, i+1, j+1
            ind 1, j+1, j-1

            r, c = 


"""