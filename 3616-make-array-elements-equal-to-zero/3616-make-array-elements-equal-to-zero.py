class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if sum(nums[:i]) == sum(nums[i:]):
                    ans+=2
                if sum(nums[:i])-1 == sum(nums[i:]):
                    ans+=1
                if sum(nums[:i]) == sum(nums[i:])-1:
                    ans+=1
        return ans