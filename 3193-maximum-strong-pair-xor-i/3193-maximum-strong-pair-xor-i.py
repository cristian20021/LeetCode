class Solution(object):
    def maximumStrongPairXor(self, nums):
        maxx = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i]-nums[j])<= min(nums[i],nums[j]):
                    if nums[i] ^ nums[j]>maxx:
                        maxx = nums[i]^nums[j]
        return maxx