class Solution(object):
    def findLHS(self, nums):
        maxx = 0 
        nums.sort()
        j = 0

        for i in range(len(nums)):
            while nums[i]- nums[j]>1:
                j+=1
            if nums[i]-nums[j]==1:
                maxx = max(maxx, i-j+1)
        return maxx