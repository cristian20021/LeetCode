class Solution(object):
    def differenceOfSums(self, n, m):
        sum1 = 0
        sum2 = 0
        for i in range(1,n+1):
            if i%m == 0:
                sum2+=i
            else:
                sum1+=i
        return sum1-sum2
        