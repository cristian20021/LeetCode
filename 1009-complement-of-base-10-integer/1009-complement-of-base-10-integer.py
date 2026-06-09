class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_rep = bin(n)[2:]
        reversed_bin = ''
        for i in binary_rep:
            if i=='1':
                reversed_bin+= '0'
            else:
                reversed_bin+= '1'
        return int(reversed_bin,2)