class Solution:
    def isSameAfterReversals(self, y: int) -> bool:
        def checker(x):
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

        if y == checker(checker(y)):
            return True
        else:
            return False
         
