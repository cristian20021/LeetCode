class Solution(object):
    def countPartitions(self, nums):
        count = 0
        for i in range(1,len(nums)):
            if (sum(nums[0:i]) - sum(nums[i:])) % 2 == 0:
                count+=1
        return count