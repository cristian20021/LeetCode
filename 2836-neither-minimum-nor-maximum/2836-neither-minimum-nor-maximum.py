class Solution(object):
    def findNonMinOrMax(self, nums):
        minn = min(nums)
        maxx  = max(nums)
        for i in nums:
            if i<maxx and i>minn:
                return i
        return -1