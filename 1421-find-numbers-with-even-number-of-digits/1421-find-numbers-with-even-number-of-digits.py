class Solution(object):
    def findNumbers(self, nums):
        evens = 0
        for i in nums:
          i = str(i)
          if len(i)% 2 == 0:
            evens+=1
        return evens
        