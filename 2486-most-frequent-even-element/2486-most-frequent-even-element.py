class Solution(object):
    def mostFrequentEven(self, nums):
        num = -1
        maxx = 0 
        a = list(set(nums))
       
        for i in a:
            if i%2 == 0:
                loc = nums.count(i)
                
                if loc>maxx:
                    num = i
                    maxx = loc
                elif loc == maxx:
                    if i<num:
                        
                        num = i
        return num