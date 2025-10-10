class Solution(object):
    def maximumEnergy(self, energy, k):
        dp = [0] * len(energy)

        for i in range(len(energy)):
            if i>=k:
                dp[i] = max(energy[i],energy[i]+dp[i-k])
            else:
                dp[i] = energy[i]

        return max(dp[len(energy)-k:])