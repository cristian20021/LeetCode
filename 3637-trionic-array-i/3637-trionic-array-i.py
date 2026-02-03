class Solution:
    def isTrionic(self, nums):
        p = 0
        q = 0

        #This loop is for increasing part(finding p)
        for i in range(1, len(nums) - 2):
            if nums[i - 1] < nums[i]:
                p = i
                continue
            break
        if p == 0:
            return False

        #Here decreasing part(finding q)
        for i in range(p + 1, len(nums) - 1):
            if nums[i - 1] > nums[i]:
                q = i
                continue
            break

        if q == 0 or q == len(nums) - 1:
            return False

        #Again checking for increasing part 
        for i in range(q + 1, len(nums)):
            if nums[i - 1] < nums[i]:
                continue
            else:
                return False
        return True