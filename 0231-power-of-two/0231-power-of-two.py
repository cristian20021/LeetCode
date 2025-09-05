class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        elif n==0:
            return False
        while n!=1:
            if n%2 == 0:
                n = n/2
            else:
                return False
        return True
        