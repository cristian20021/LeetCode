class Solution(object):
    def largestPerimeter(self, nums):
        maxxPer = 0
        nums = sorted(nums)
        i = len(nums)-1
        while i>1:
            if nums[i]<nums[i-1]+nums[i-2]:
                return nums[i]+nums[i-1]+nums[i-2]
            i-=1
        return maxxPer