class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0  
        while target > 1: 
            if maxDoubles > 0 and target % 2 == 0:  
               
                target //= 2
                maxDoubles -= 1
            else:
               
                if maxDoubles == 0:
                    count += target - 1 
                    break
                target -= 1
            count += 1

        return count
