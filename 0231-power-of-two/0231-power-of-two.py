class Solution:
    def helper(self, n):
        if n == 1:
            return True
        if n < 1:
            return False
        return self.helper(n/2)

    def isPowerOfTwo(self, n: int) -> bool:
        return self.helper(n)