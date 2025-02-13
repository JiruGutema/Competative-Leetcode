class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        i = 0
        for i in range(len(costs)):
            if coins >= costs[i]:
                count += 1
                coins -= costs[i]
                i += 1
            else:
                break
            
        return count

