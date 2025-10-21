class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        return (s.count('1')-1)*'1' + s.count('0')*'0'+'1'
        
        