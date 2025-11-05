class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """

        
        for j in range(len(num)):
            if int(num[j]) != num.count(str(j)):

                return False
        return True
            