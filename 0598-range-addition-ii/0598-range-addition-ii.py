class Solution(object):
    def maxCount(self, m, n, ops):
        if len(ops)==0:
            return m*n
        minZ = 999999
        minF = 999999

        for i in range(len(ops)):
            if ops[i][0]<minZ:
                minZ = ops[i][0]
            if ops[i][1]<minF:
                minF = ops[i][1]

        return minZ*minF