class Solution(object):
    def maxFreqSum(self, s):
        maxV = 0
        maxC = 0
        countDict = {}
        vowels = ['a','e','i','o','u']

        for i in s:
            if i not in countDict:
                countDict[i]=1
            else:
                countDict[i]+=1
        
        for key, value in countDict.items():
            if key in vowels:
                if value>maxV:
                    maxV = value
            else:
                if value>maxC:
                    maxC = value
        return maxC+maxV
        