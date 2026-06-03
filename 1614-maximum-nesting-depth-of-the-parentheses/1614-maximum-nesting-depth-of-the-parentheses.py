class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxx = 0
        count = 0
        for i in s:
            
            if i == "(":
                count += 1
                if count>maxx:
                    maxx = count
            elif i == ")":
                count-=1
        return maxx
