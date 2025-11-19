class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        
        for i in range(len(nums)+1):
            if original in nums:
                original = 2 * original
            else:
                return original