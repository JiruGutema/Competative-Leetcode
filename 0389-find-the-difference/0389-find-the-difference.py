class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = 0
        combined = s+t

        for ch in combined:
            a ^= ord(ch)
        return chr(a)