class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''
        for i in s:
            if i.isalnum():
                a = a+(i.lower())
        if a == a[::-1]:
            return True
        else:
            return False
        