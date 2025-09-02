class Solution(object):
    def maximumDifference(self, nums):
        maxDif = -1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>=nums[j]:
                    break
                else:
                    loc = nums[j]-nums[i]
                    if loc > maxDif:
                        maxDif = loc
        return maxDif
        