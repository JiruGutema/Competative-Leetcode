class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
  
        if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
            return False
        
        if desiredTotal <= 0:
            return True
        
        memo = {}
        
        def can_win(used_numbers, current_total):
            if (used_numbers, current_total) in memo:
                return memo[(used_numbers, current_total)]
            
            for i in range(maxChoosableInteger):
                if not (used_numbers & (1 << i)):
                    if current_total - (i + 1) <= 0 or not can_win(used_numbers | (1 << i), current_total - (i + 1)):
                        memo[(used_numbers, current_total)] = True
                        return True
            
            memo[(used_numbers, current_total)] = False
            return False
        
        return can_win(0, desiredTotal)
