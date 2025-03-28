class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s:
            return s
        
        def check(s, char):
            if char.islower():
                return char.upper() in s
            else:
                return char.lower() in s

        def recursion(s):
            for i in range(len(s)):
                if not check(s, s[i]):
                    s1 = recursion(s[:i])
                    s2 = recursion(s[i+1:])
                    return s2 if len(s2) > len(s1) else s1 
            return s 

        return recursion(s)
