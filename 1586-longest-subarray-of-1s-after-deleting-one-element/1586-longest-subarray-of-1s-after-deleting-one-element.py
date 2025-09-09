class Solution(object):
    def longestSubarray(self, nums):
        dp = []
        count = 0

        for i in nums:
            if i == 1:
                count +=1
            else:
                dp.append(count)
                count = 0
        dp.append(count)

        if len(dp) == 1:
            return dp[0] - 1
        maxx = 0
        for j in range(len(dp)-1):   
            if dp[j]+dp[j+1] > maxx:
                maxx = dp[j]+dp[j+1]
        return maxx