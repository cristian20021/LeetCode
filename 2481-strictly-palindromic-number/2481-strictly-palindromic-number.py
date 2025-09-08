class Solution(object):
    def numberToBase(self,n, b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        return digits[::-1]
    def isStrictlyPalindromic(self, n):
        for i in range(2,n-1):
            local = str(self.numberToBase(n,i))
            if local != local[::-1]:
                return False
        return True
        