class Solution:
    def maxScore(self, s: str) -> int:

        length = len(s)
        counter = Counter(s)
        ones = counter["1"]
        zeros = 0

        ans = 0 

        for i in range(length -1):
            if s[i] == '1':
                ones -= 1
                 
            else:
                zeros += 1

            ans = max(zeros + ones, ans)
        return ans 