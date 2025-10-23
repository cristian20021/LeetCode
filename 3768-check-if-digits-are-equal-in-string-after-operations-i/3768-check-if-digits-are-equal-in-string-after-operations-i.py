class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while len(s)>2:
            newNum=''
            for i in range(len(s)-1):
                new = (int(s[i])+int(s[i+1]))%10
                newNum+=str(new)
            s=newNum
   
        if s[0] == s[1]:
            return True
        return False