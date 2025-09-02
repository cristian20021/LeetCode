class Solution(object):
    def maxSum(self, nums):
        newL = []
      
        for i in nums:
            if i not in newL and i>0:
                newL.append(i)
        if len(newL) == 0:
            return max(nums)
        return sum(newL)
        