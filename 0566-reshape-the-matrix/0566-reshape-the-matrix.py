class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        if len(mat)*len(mat[0]) != r*c:
            return mat
        
        linearArr = []
        finalArr = []

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                linearArr.append(mat[row][col])

        count = 0

        for row in range(r):
            localArr = []
            for col in range(c):
                localArr.append(linearArr[count])
                count+=1
            finalArr.append(localArr)

        return finalArr

        