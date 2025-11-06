class Solution(object):
    def numberOfChild(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
  
        if (k // (n-1)) % 2 == 0:

            return k%(n-1)
        else:

            return n-1-(k%(n-1))