class Solution(object):
  
        
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == sorted(nums):
            return True

        for i in range(len(nums)):
            localArr = []
            localArr.append(nums[-1])
            for j in range(len(nums)-1):
                localArr.append(nums[j])
            if localArr == sorted(localArr):
                return True
            nums = localArr
        return False