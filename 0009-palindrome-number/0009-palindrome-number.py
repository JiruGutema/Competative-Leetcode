class Solution:
    def isPalindrome(self, x: int) -> bool:
        i = 0
        string  = str(x)
        j = len(string)-1

        while j > i:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True
