class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        count_ops=0
        val=k
        while val>1:
            jumps= math.ceil(math.log2(val))
            val -= 2**(jumps-1)
            count_ops+=operations[jumps-1]
        return chr(ord('a')+(count_ops%26))