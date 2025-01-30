class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2 ==0:
            return n

        num = max(n, 2)
        num = (num) if num%2==0 else (num+1)
        
        while True:
            if num % n == 0 and num % 2==0:
                return num
            else:
                num += 2