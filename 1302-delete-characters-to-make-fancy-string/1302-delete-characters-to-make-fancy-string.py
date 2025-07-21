class Solution(object):
    def makeFancyString(self, s):
        
        count = 0
        newS = s[0]
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count+=1
                if count > 1:
                    pass
                else:
                    newS+=s[i]
            else:
                count = 0
                newS+=s[i]
        return newS