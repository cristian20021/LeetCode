class Solution(object):
    def minOperations(self, nums):
            for i in range(len(nums)):
                    if nums[i] != nums[0]:
                        return 1
            return 0