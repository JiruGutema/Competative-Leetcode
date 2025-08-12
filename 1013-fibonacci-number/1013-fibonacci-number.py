class Solution:
    def fib(self, n: int) -> int:
        # top down
        # memo = {0:0, 1:1}

        # def dp(n):
        #     if n in memo:
        #         return memo[n]
        #     else:
        #         memo[n] = dp(n-1) + dp(n-2)
        #     return memo[n]
        # return dp(n)
        
        # bottom up

        if n <= 1:
            return n
            
        memo = [0]*(n+1)
        memo[1] = 1
        base = 2

        while base < n+1:
            memo[base] = memo[base-1] + memo[base-2]
            base += 1
        return memo[base - 1]





