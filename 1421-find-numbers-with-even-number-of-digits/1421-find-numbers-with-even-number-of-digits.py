class Solution(object):
    def findNumbers(self, nums):
        evens = 0
        for i in nums:
            if i>9 and i<100 or i>999 and i<10000 or i == 100000:
                evens+=1
        return evens
        