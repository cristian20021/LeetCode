class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_list = []

        for i in nums:
            new_list.append(nums[i])
        
        return new_list