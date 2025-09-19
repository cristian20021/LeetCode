class Solution(object):
    def dominantIndex(self, nums):
        maxx = max(nums)
        indexMax = nums.index(maxx)
        nums.remove(maxx)
  
        for i in nums:
            if i*2 <=maxx:
                pass
            else:
                return -1
        return indexMax