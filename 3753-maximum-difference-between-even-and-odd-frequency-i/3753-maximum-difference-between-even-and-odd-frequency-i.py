class Solution(object):
    def maxDifference(self, s):

        # highest odd - min even
        dictS = {}
        for i in s:
            if i not in dictS:
                dictS[i] = 1
            else:
                dictS[i]+=1
        maxxOdd = 0
        minEven = 999999
        for key, value in dictS.items():
            if value % 2 != 0:
                if value > maxxOdd:
                    maxxOdd = value
            else:
                if value< minEven:
                    minEven = value
        return maxxOdd - minEven
        