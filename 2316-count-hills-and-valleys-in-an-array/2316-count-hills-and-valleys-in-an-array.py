class Solution(object):
    def countHillValley(self, nums):
        count = 0 
        j = 0
        for i in range(1,len(nums)-1):
            if (nums[j]>nums[i]<nums[i+1]) or (nums[j]<nums[i]>nums[i+1]):
                count+=1
                j=i
        
        return count
        