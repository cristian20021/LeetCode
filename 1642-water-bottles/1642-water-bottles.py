class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        return int(numBottles + (numBottles - 1) / (numExchange - 1))

        