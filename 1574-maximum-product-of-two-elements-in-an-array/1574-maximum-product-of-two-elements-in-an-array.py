class Solution(object):
    def maxProduct(self, nums):
        copy = nums[:]
        maxx1 = max(nums)
        copy.remove(maxx1)
        maxx2 = max(copy)
        return (maxx1-1)*(maxx2-1)
        