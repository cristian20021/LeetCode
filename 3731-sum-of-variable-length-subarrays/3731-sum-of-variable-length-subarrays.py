class Solution(object):
    def subarraySum(self, nums):
        summ = 0
        for i in range(len(nums)):
            start =  max(0,i-nums[i])
         
            summ += sum(nums[start:i+1])
        return summ