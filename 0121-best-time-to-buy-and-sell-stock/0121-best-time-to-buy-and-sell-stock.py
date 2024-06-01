class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = float('inf')
        maxsell=0
        for i in range (0,len(prices)):
            minbuy=min(minbuy,prices[i])
            maxsell=max(maxsell,prices[i]-minbuy)
        return maxsell
        """The key steps are:

        It initializes two variables: minbuy and maxsell.
        minbuy keeps track of the minimum stock price seen so far.
        maxsell keeps track of the maximum profit that can be obtained.
        It iterates through the prices list.
        For each price prices[i], it updates minbuy to be the minimum of the current minbuy and prices[i].
        It then updates maxsell to be the maximum of the current maxsell and the difference between prices[i] and minbuy.
        Finally, it returns the maximum profit stored in maxsell."""