class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        weeks = n//7
        days = n%7
        summ=0
        if weeks==0:
            for i in range(1,days+1):
                summ+=i
        
        else:
            for i in range(1,days+1):
                summ+=i+weeks
            for j in range(weeks):
                summ+=28+(j*7)
        return summ