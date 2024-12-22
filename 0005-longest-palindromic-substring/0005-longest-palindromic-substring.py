class Solution:
    def longestPalindrome(self, s: str) -> str:

        curr = ''
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    if len(curr) < len(s[i:j]):
                        curr = s[i:j]
        return curr