class Solution(object):

    def maxSubsequence(self, nums, k):
        indexed = [(val, idx) for idx, val in enumerate(nums)]

        indexed.sort(key=lambda x: -x[0])

        topk = sorted(indexed[:k], key=lambda x: x[1])
        return [val for val, idx in topk]