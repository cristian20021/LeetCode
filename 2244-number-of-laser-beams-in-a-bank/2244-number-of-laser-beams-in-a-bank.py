class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """

        lasers = []
        for i in range(len(bank)):
            localSum = 0
            for j in range(len(bank[i])):
                if bank[i][j] == '1':
                    localSum+=1
            if localSum!=0:
                lasers.append(localSum)
        final = 0
        for z in range(len(lasers)-1):
            final+= lasers[z]*lasers[z+1]
        return final