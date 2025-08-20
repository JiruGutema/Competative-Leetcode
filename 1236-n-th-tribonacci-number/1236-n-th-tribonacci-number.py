class Solution:
    def tribonacci(self, n: int) -> int:
     
        if n < 2:
            return n
        
        first, second, third = 0,1,1

        for i in range(3, n + 1):
            next_val = first + second + third
            first, second, third = second, third, next_val

        return third