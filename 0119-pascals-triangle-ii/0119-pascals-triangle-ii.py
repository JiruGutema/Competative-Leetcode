class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1] for i in range(rowIndex+2)]
        if rowIndex >1:
            ans[1].append(1)
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        for i in range(2, rowIndex+2):
            n,m = 0,1
            while m < (len(ans[i-1])):
                ans[i].append(ans[i-1][n]+ans[i-1][m])
                n += 1
                m += 1
            ans[i].append(1)
        ans.pop()
        return ans.pop()
            
