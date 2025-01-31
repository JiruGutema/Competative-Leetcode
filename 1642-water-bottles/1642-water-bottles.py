class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # return numBottles + (numBottles-1)//(numExchange-1)

        empty = numBottles
        drinked = numBottles

        while empty >= numExchange:
            drinked += empty//numExchange
            empty += empty//numExchange - ((empty//numExchange) *numExchange)
        return drinked
