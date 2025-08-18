class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxx = 0
        count = 0
        for i in nums:
            if i == 1:
                count +=1
            else:
                if count > maxx:
                    maxx = count
                count = 0
        if count>maxx:
            return count
        return maxx