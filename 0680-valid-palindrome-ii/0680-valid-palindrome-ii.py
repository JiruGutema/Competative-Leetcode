class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True


        i = 0
        j = len(s)-1

        while i < j:
            if s[i] == s[j]:
                j -= 1
                i += 1
            else:
                condition1 = helper(i, j-1)
                condition2 = helper(i+1, j)

                return condition1 or condition2
        return True
        
    
            