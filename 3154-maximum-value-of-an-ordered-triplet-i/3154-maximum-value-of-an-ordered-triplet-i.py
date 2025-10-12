class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxx = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for z in range(j+1,len(nums)):
                    if nums[i] < 0 and nums[j]<0 and nums[z]< 0:
                        return 0
                    else:
                        if ((nums[i] - nums[j]) * nums[z])>maxx:
                            maxx = (nums[i] - nums[j]) * nums[z]
        return maxx