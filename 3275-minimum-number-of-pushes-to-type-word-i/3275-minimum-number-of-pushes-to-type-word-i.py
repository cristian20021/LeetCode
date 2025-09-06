class Solution(object):
    def minimumPushes(self, word):
        i = 0
        summ = 0
        while i<len(word):
            summ += i//8 + 1
            i+=1
        return summ