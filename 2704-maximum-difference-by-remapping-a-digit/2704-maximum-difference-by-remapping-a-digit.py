class Solution(object):
    def minMaxDifference(self, num):
        minNumStr = str(num)
        newMin = ''
        for i in range(len(minNumStr)):
            if minNumStr[i] == minNumStr[0]:
                newMin+='0'
            else:
                newMin+=minNumStr[i]
        print(newMin)

        maxNumStr = str(num)
        newMax = ''

        maxTBR = ''
        for x in maxNumStr:
            if x!= '9':
                maxTBR = x
                break

        for i in range(len(maxNumStr)):
            if maxNumStr[i]== maxTBR:
                newMax+='9'
            else:
                    newMax+=maxNumStr[i]
        print(newMax)
        return int(newMax)- int(newMin)