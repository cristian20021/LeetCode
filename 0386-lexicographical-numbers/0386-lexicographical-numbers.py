class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        fin = []
        for i in range(1,n+1):
            fin.append(str(i))
     
        return list(map(int, sorted(fin) ))