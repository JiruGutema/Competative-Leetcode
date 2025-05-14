class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        count = 0

        while n:
            count += 1
            n = n & n - 1
        return count
