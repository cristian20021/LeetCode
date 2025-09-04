class Solution(object):
    def findClosest(self, x, y, z):
        if abs(x-z)<abs(y-z):
            return 1
        elif abs(x-z)>abs(y-z):
            return 2
        else:
            return 0