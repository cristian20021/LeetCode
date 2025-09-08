class Solution(object):
    def containZeros(self,numStr):
        for j in numStr:
            if j == '0':
                return False
        return True
    def getNoZeroIntegers(self, n):
        for i in range(1,n):
            if self.containZeros(str(i)) and self.containZeros(str(n-i)):
                return [i,n-i]