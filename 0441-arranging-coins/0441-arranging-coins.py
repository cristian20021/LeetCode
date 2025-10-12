class Solution(object):
    def arrangeCoins(self, n):
        rowLen = 1
        count = 0
        
        while n>=rowLen:
                count+=1
                n-=rowLen
                rowLen+=1
        return count