class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans = 0
        i = 0
        chemistry = skill[0]+skill[-1]
        j = len(skill) -1
        while i < j:
            temp = (skill[j]+skill[i])
            if temp == chemistry:
                ans += (skill[j]*skill[i])
            else:
                return -1
            i += 1
            j -= 1
        return ans
