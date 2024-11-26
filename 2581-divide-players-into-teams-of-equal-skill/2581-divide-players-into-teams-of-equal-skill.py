from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans = []
        
        chemistry = 0
        i = 0
        j = len(skill)-1
        product = skill[i]+skill[j]
        while i <= j:
            chemistry += skill[i]*skill[j]
            
            if skill[i]+skill[j] != product:
                return -1
            product = skill[i]+skill[j]
            i+= 1
            j -= 1

        return chemistry