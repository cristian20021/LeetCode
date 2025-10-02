class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        maxx = 0
        empty = 0
        while numBottles>0:
            maxx += numBottles
            empty += numBottles
            numBottles = 0
            while empty>=numExchange:
                numBottles+=1
                empty -= numExchange
                numExchange+=1
        return maxx

        