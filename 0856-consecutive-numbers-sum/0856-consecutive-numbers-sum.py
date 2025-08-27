class Solution(object):
    def consecutiveNumbersSum(self, N):
            import math
            
            count = 0
            n = 2
            target = math.sqrt(2*N)
            while n < target:
                if (N - n*(n-1)/2) % n == 0:
                    count += 1
                n += 1
            return count+1