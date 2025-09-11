class Solution(object):

    def minOperations(self, s):
        alph = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        minn = 26
        if len(s) == 1:
            if s[0]!='a':
                return 26 - alph.index(s[0])
            else:
                return 0
        for i in s:
            if i != 'a':
                if alph.index(i)<minn:
                    minn = alph.index(i)
        return 26 - minn

                
                