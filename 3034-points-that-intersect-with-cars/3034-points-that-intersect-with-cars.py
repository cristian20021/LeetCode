class Solution(object):
    def numberOfPoints(self, nums):
        toRet = []
        for i in range(len(nums)):
            for j in range(nums[i][0],nums[i][1]+1):
                toRet.append(j)
        
        a = list(set(toRet))
        return len(a)
        