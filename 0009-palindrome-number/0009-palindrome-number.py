class Solution:
    def isPalindrome(self, x: int) -> bool:
        xf = str(x)
        xr = xf[::-1]
        if xf == xr:
            return True
        else:
            return False