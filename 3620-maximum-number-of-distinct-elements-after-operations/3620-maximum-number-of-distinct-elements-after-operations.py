class Solution(object):
    def maxDistinctElements(self, nums, k):
        nums = sorted(nums)
        c = -10**10
        ans = 0
        for i in nums:
            l = i-k
            r = i+k
            if c<l:
                c = l
            if c<=r:
                ans+=1
                c+=1
        return ans