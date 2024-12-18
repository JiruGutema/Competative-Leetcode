class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        N = len(prices)
        for i,p in enumerate(prices):
            for index2 in range(i+1,N):
                p2 = prices[index2]
                if p2 <= p :
                    ans.append(p-p2)
                    break
            else:
                ans.append(p)
        return ans
