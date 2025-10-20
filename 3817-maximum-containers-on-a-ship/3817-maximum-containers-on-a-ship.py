class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        """
        :type n: int
        :type w: int
        :type maxWeight: int
        :rtype: int
        """
        load = 0
        containers = 0
        for i in range(n*n):
            load+=w
            containers+=1
            if load>maxWeight:
                return containers-1
        return n*n