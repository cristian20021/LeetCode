class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squaredList = []

        for i in nums:
            squaredList.append(i*i)
        
        return sorted(squaredList)
        