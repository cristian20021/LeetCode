class Solution(object):
    def countOdds(self, low, high):
        if high%2 == 0 and low%2==0:
            return (high-low)/2
        else:
            return (high-low+2)/2