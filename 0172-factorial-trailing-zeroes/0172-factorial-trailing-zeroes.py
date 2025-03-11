class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * fact(n - 1)
        factorial = fact(n)
        count = 0
        while factorial > 0:
            if factorial%10 == 0:
                count += 1
                factorial //= 10
            else:
                break
        return count
    
