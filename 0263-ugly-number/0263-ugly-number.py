class Solution(object):
    def isUgly(self, n):
        for i in range(31):
            for j in range(20):
                for z in range(13):
                    if (2**i)*(3**j)*(5**z) == n:
                        return True
        return False
        