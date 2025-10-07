class Solution(object):
    def maxDivScore(self, nums, divisors):
        maxx = 0
        num = 10000000000000000
        for i in range(len(divisors)):
            count = 0
            for j in range(len(nums)):
                if nums[j]%divisors[i] == 0:
                    count+=1
            if count>maxx:
                maxx = count
                num = divisors[i]
            elif count == maxx:
                if divisors[i]<num:
                    num = divisors[i]
        return num