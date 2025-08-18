class Solution(object):
    def maximum69Number (self, num):
        numStr = str(num)
        for i in range(len(numStr)):
            if numStr[i] == '6':
                numStr = numStr[:i] + '9' + numStr[i+1:]
                break
        return int(numStr)

        