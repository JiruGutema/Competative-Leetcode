class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n - 1)
        facted = fact(n)
        count = 0
        while facted > 0:
            if facted%10 == 0:
                count += 1
                facted //= 10
            else:
                break
        return count
    
