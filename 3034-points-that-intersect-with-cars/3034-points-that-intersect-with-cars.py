class Solution(object):
    def numberOfPoints(self, nums):
        toRet = []
        for i in range(len(nums)):
            for j in range(nums[i][0],nums[i][1]+1):
                if j not in toRet:
                    toRet.append(j)
        
        
        return len(toRet)
        