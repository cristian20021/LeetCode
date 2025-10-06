class Solution(object):
    def triangleNumber(self, nums):
        count = 0
        nums = sorted(nums)
        for i in range(len(nums)-1,1,-1):
            l = 0
            r = i-1
            while l<r:
                if nums[l]+nums[r]>nums[i]:
                    count+= r-l
                    r-=1
                else:
                    l+=1
        return count
