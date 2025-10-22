class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)

        if n == 0: return 0

        left = 0
        right = 0
        sumCount = 0
        result = 0
        left2 = 0
        sumCount2 = 0
        count = 0
        prev = None

        for num in nums:
            if num == prev:
                count += 1
            else:
                prev = num
                count = 1

            while nums[left] < num - k:
                sumCount -= 1
                left += 1

            while right < n and nums[right] <= num + k:
                sumCount += 1
                right += 1

            result = max(result, count + min(sumCount - count, numOperations))

            sumCount2 += 1
            while nums[left2] < num - 2 * k:
                sumCount2 -= 1
                left2 += 1

            result = max(result, min(sumCount2, numOperations))

        return result
        