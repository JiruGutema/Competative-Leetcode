class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            t = sorted(t)
            s = sorted(s)
            if t == s:
                return True
            else:
                return False
                