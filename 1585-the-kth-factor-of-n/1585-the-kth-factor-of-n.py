class Solution(object):
    def kthFactor(self, n, k):
        factors = []
        for i in range(1,n+1):
            if n%i == 0:
                factors.append(i)
        try:
            return factors[k-1]
        except:
            return -1