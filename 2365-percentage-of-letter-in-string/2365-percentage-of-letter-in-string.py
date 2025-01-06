class Solution(object):
    def percentageLetter(self, s, letter):
        count = 0 
        for i in s:
            if i==letter:
                count+=1
        return int(round(count*100/len(s)))