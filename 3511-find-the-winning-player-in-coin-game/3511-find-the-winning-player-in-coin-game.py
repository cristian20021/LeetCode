class Solution(object):
    def winningPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """
        count = 0
        
        while x>=1 and y>=4:
                count+=1
                x-=1
                y-=4
        if count%2==0:
            return 'Bob'
        return 'Alice'
        