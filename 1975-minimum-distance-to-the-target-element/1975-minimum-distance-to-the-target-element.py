class Solution(object):
    def getMinDistance(self, nums, target, start):
        minn = 1001
        for i in range(len(nums)):
            if nums[i] == target:
                if abs(i-start)<minn:
                    minn = abs(i-start)
        return minn