class Solution(object):
    def smallestAbsent(self, nums):
 
        average = sum(nums)//len(nums)
        if average<0:
            toRet = 1
        else:
            toRet = average+1
        while toRet in nums:
            toRet+=1
        return toRet