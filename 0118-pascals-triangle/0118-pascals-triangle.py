class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1] for i in range(numRows+1)]
        ans[1].append(1)
        for i in range(2, numRows):
            n,m = 0,1
            while m < (len(ans[i-1])):
                ans[i].append(ans[i-1][n]+ans[i-1][m])
                n += 1
                m += 1
            ans[i].append(1)
        ans.pop()
        return ans
            
