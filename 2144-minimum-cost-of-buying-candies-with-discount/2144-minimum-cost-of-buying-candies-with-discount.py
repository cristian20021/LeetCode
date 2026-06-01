class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost)<3:
            return sum(cost)
        cost.sort(reverse = True)

        summ = 0
        for i in range(len(cost)):
            if (i+1)%3 != 0:
                summ += cost[i]
        return summ
            