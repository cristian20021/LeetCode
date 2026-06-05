class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        col = {'}':'{',']':'[',')':'('}
        stack = []
        for i in s:
            if i == '[' or i=='{' or i == '(':
                stack.append(i)
            else:
                try:
                    if col[i] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                except:
                    return False
        if len(stack) == 0:
            return True
        return False        