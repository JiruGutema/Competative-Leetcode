class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        p = sorted(p)
        start = 0
        end = k
        ans = []

        while end < len(s)+1:
            if p == sorted(s[start:end]):
                ans.append(start)
            start += 1
            end += 1
        return ans