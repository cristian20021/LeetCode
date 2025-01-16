class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxx = max(candies)
        l = []
        for i in candies:
            if i+extraCandies >= maxx:
                l.append(True)
            else:
                l.append(False)
        return l