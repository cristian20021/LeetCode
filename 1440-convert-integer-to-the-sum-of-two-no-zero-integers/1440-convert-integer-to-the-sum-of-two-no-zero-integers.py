class Solution(object):
    def containZeros(self,numStr):
        for j in numStr:
            if j == '0':
                return False
        return True
    def getNoZeroIntegers(self, n):
        for i in range(1,n):
            iLocal = self.containZeros(str(i))
            restLocal = self.containZeros(str(n-i))
            if iLocal == True and restLocal == True:
                return [i,n-i]