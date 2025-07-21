class Solution(object):
    def makeFancyString(self, s):
        
        newS = ''
        if len(s)<3:
            return s
        for i in range(len(s)-2):
            if s[i]==s[i+1] and s[i+1] == s[i+2]:
                pass
            else:
                newS+=s[i]
        return newS+s[-2]+s[-1]