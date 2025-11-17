class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        countAv = False
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 1 and countAv == False:
                countAv = True
            elif countAv == True:
                if nums[i] == 0:
                    zeros+=1
                else:
                    if zeros < k:
                        return False
                    else:
                        zeros = 0
        return True
                
