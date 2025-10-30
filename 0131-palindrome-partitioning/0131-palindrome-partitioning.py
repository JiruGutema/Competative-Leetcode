class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def isPalandrome(string):
            return string == string[::-1]

        def backtrack(idx):
            if (idx == len(s)):
                ans.append(path[:])
                return


            for i in range(idx, len(s)):
                sub = s[idx: i+1]
                if(isPalandrome(sub)):
                    path.append(sub)
                    backtrack(i + 1)
                    path.pop()
        backtrack(0)

        return ans