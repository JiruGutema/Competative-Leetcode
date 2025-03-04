class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda costs: (costs[0]-costs[1]), reverse=True)
        greedy_A = sum(cost[0] for cost in costs)

        for i in range(len(costs)//2):
            greedy_A -= costs[i][0]
            greedy_A += costs[i][1]
        return greedy_A