class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closestInt = nums[0]
        
        for i in nums:
            if abs(i)<abs(closestInt):
                closestInt = i
            elif abs(i) == abs(closestInt):
                if i > closestInt:
                    closestInt = i
        return closestInt