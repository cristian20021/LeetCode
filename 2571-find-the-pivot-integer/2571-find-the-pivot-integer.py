class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst = [i+1 for i in range(n)]
        if n == 1:
            return 1
        for j in range(1,len(lst)):
            if sum(lst[:j+1]) == sum(lst[j:]):
                return j+1
        return -1
        