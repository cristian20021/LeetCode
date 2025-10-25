class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        summ = 0
        mondCount = 0
        for i in range(1,n+1):
            if i%7 == 0:
                summ+=mondCount + 7
                mondCount+=1
            else:
                summ+=mondCount+(i%7)
        return summ