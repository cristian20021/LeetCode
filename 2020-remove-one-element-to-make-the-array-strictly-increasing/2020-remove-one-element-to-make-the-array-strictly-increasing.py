class Solution(object):
    def check(self,List):
        
        for j in range(len(List)-1):
            if List[j]>=List[j+1]:
                return False

        return True
            
    def canBeIncreasing(self, nums):
        count = 0

        for i in range(len(nums)):  
            newL = nums[:]
            del newL[i]
            a = self.check(newL)
            if a == True:
                count+=1

        if count > 0:
            return True

        return False