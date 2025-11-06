class Solution(object):
    def check(self, substr):

        for i in range(len(substr)):
            if substr[i].isupper() and substr[i].lower() not in substr:
                return False
            if substr[i].islower() and substr[i].upper() not in substr:
                return False
        
        return True
   

    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxx = 0
        maxSub = ''
        if len(s) == 2:
            if s[0].lower() == s[1].lower() and s[0]!=s[1]:
                return s
            else:
                return ""

        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if self.check(s[i:j]) == True:
                    if len(s[i:j]) > maxx:
                        maxx = len(s[i:j])
                        maxSub = s[i:j]
        return maxSub