class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        countLst = []
        for i in nums:
            if i == 1:
                count +=1
            else:
                countLst.append(count)
                count = 0
        countLst.append(count)
        return max(countLst)