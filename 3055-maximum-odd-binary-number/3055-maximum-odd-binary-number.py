class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        zeros = s.count('0')
        ones = s.count('1')

        if ones == 1:
            return zeros*'0'+'1'
        
        return (ones-1)*'1' + zeros*'0'+'1'
        
        