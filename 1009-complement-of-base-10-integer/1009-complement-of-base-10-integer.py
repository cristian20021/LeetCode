class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        reversed_int = 0
        bin_n = bin(n)[2:]
        ind = len(bin_n)-1
        for i in bin_n:
            if i == "0":
                reversed_int+= 2**ind
            ind-=1
        return reversed_int
