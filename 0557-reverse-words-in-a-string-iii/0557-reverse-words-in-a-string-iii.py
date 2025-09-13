class Solution(object):
    def reverseWords(self, s):
        s  = s+' '
        finalS = ''
        localS = ''
        for i in s:
            if i == ' ':
                finalS+=localS[::-1] + ' '
                localS = ''
            else:
                localS+=i
        return finalS[:len(s)-1]