class Solution(object):
    def maxPower(self, s):
        if len(s)==1:
            return 1
        maxx = 0
        count = 1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                count +=1
            else:
                if count > maxx:
                    maxx = count
           
                count = 1
        if count>maxx:
            return count
        return maxx