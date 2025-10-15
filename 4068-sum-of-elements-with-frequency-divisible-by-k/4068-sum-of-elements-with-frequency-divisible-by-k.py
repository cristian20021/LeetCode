class Solution(object):
    def sumDivisibleByK(self, nums, k):
        rec = {}
        summ = 0
        for i in nums:
            if i not in rec:
                rec[i] = 1
            else:
                rec[i] += 1
        for key,value in rec.items():
            if value%k == 0:
                summ += key*value
        return summ