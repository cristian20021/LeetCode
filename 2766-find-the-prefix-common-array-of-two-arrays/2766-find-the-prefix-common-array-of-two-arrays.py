class Solution(object):
    def check(self,A,B):
        toRet = 0
        for i in A:
            if i in B:
                toRet+=1
        return toRet

    def findThePrefixCommonArray(self, A, B):
        finalL = []

        for i in range(len(A)):
            temp = self.check(A[:i+1],B[:i+1])
            finalL.append(temp)
        return finalL