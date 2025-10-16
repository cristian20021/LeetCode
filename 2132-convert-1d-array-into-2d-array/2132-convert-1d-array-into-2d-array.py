class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """

        finalArr = []
        count = 0

        if m * n != len(original):
            return []

        for row in range(m):
            localArr = []
            for column in range(n):
                localArr.append(original[count])
                count+=1
            finalArr.append(localArr)
        return finalArr