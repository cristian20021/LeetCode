class Solution(object):
    def maxFrequencyElements(self, nums):
        uniq = list(dict.fromkeys(nums))
        maxx = 0
        for i in uniq:
            if nums.count(i)>maxx:
                maxx = nums.count(i)
        ret = 0
        for j in uniq:
            if nums.count(j) == maxx:
                ret+=maxx
        return ret