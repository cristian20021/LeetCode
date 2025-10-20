class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxx = 0
        localSum = nums[0]
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                localSum+=nums[i+1]
            elif nums[i]>=nums[i+1]:
                if localSum>maxx:
                    maxx = localSum
                localSum = nums[i+1]
        if localSum>maxx:
            return localSum
        return maxx