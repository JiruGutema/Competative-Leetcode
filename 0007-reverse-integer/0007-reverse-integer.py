class Solution:
    def reverse(self, x: int) -> int:
        signed = False
        if x<0:
            signed = True
        numStr = str(x)
        
        numStr = numStr[::-1]
        if signed:
            numStr = numStr[:len(str(x))-1]
            numStr = '-'+numStr
        if ((int(numStr) < -2147483648) or (int(numStr) > 2147483647)):
            return 0
        return int(numStr)