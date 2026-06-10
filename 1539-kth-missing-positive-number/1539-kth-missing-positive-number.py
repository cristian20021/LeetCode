class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        missing = []
        
        for i in range(1,10000):
                if i not in arr:
                    missing.append(i)
                if len(missing) == k:
                    break
        return missing[-1]