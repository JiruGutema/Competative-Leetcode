class Solution:
    MOD = 10**9 + 7
    def countGoodNumbers(self, n: int) -> int:
 
        
        e = (n + 1) // 2
        o = n // 2

        e_w = self.pow(5, e)
        o_w = self.pow(4, o)
        return (e_w * o_w) % self.MOD

    def pow(self, base, power):
        result = 1
        base %= self.MOD
        while power > 0:
            if power % 2 == 1:
                result = (result * base) % self.MOD
            base = (base * base) % self.MOD
            power //= 2

        return result