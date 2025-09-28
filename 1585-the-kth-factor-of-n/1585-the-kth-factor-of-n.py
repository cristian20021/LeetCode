class Solution(object):
    def kthFactor(self, n, k):
        factors = []
        for i in range(1,n+1):
            if n%i == 0:
                factors.append(i)
        if len(factors)<k:
            return -1
        return factors[k-1]
